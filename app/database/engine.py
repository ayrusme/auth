"""
This file takes care of the engine decalaration
"""
from sqlalchemy import create_engine
from sqlalchemy import event
from sqlalchemy import exc
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from app.config.config import DB_URI
from app.helpers.codes import MUGGLE
from app.helpers.codes import STORM_TROOPER
from app.helpers.codes import VADER

SESSION = scoped_session(sessionmaker())

_ENGINE = create_engine(
    DB_URI, {
        "encoding": "utf-8",
    },
)
try:
    _ = _ENGINE.connect()
except exc.DBAPIError:
    _ENGINE = create_engine(
        DB_URI, {
            "encoding": "utf-8",
        },
    )
SESSION.remove()
SESSION.configure(bind=_ENGINE, autoflush=False, expire_on_commit=False)
Base.metadata.create_all(_ENGINE)


@event.listens_for(_engine, "engine_connect")
def ping_connection(connection, branch):
    if branch:
        # "branch" refers to a sub-connection of a connection,
        # we don't want to bother pinging on these.
        return

    # turn off "close with result".  This flag is only used with
    # "connectionless" execution, otherwise will be False in any case
    save_should_close_with_result = connection.should_close_with_result
    connection.should_close_with_result = False

    try:
        # run a SELECT 1.   use a core select() so that
        # the SELECT of a scalar value without a table is
        # appropriately formatted for the backend
        connection.scalar(select([1]))
    except exc.DBAPIError as err:
        # catch SQLAlchemy's DBAPIError, which is a wrapper
        # for the DBAPI's exception.  It includes a .connection_invalidated
        # attribute which specifies if this connection is a "disconnect"
        # condition, which is based on inspection of the original exception
        # by the dialect in use.
        if err.connection_invalidated:
            # run the same SELECT again - the connection will re-validate
            # itself and establish a new connection.  The disconnect detection
            # here also causes the whole connection pool to be invalidated
            # so that all stale connections are discarded.
            connection.scalar(select([1]))
        else:
            raise
    finally:
        # restore "close with result"
        connection.should_close_with_result = save_should_close_with_result


# INIT ROLES
DB_SESSION = SESSION()
SUPER_ADMIN_ROLE = Role(**VADER)
ADMIN_ROLE = Role(**STORM_TROOPER)
USER_ROLE = Role(**MUGGLE)

try:
    RESULT = DB_SESSION.query(Role).filter(
        Role.role_id == SUPER_ADMIN_ROLE.role_id,
    ).first()
    if not RESULT:
        print("Adding VADER")
        DB_SESSION.add(SUPER_ADMIN_ROLE)
    RESULT = DB_SESSION.query(Role).filter(
        Role.role_id == USER_ROLE.role_id,
    ).first()
    if not RESULT:
        print("Adding Muggles")
        DB_SESSION.add(USER_ROLE)
    RESULT = DB_SESSION.query(Role).filter(
        Role.role_id == ADMIN_ROLE.role_id,
    ).first()
    if not RESULT:
        print("Adding Storm Troopers to manage the muggles")
        DB_SESSION.add(ADMIN_ROLE)
    DB_SESSION.commit()
except IntegrityError as exp:
    print(exp)
    print("Seems like the roles are added")
except Exception as exp:
    print(exp)
    DB_SESSION.rollback()
