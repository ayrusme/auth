"""
This file takes care of the engine decalaration
"""
from sqlalchemy import create_engine, event, exc, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import scoped_session, sessionmaker

from config.config import DB_URI
from helpers.codes import REBEL, STORM_TROOPER, VADER

from . import Base, Role

SESSION = scoped_session(sessionmaker())

_ENGINE = create_engine(DB_URI)

try:
    _ = _ENGINE.connect()
except exc.DBAPIError:
    _ENGINE = create_engine(
        DB_URI, {
            "encoding": "utf-8"
        }
    )
SESSION.remove()
SESSION.configure(bind=_ENGINE, autoflush=False, expire_on_commit=False)
try:
    Base.metadata.create_all(_ENGINE)
except Exception as exp:
    # Multiple workers will try to insert the same schema
    # Handle it gracefully
    print("The workers are trying to fuck up the system")


@event.listens_for(_ENGINE, "engine_connect")
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
USER_ROLE = Role(**REBEL)

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
        print("Adding Rebels")
        DB_SESSION.add(USER_ROLE)
    RESULT = DB_SESSION.query(Role).filter(
        Role.role_id == ADMIN_ROLE.role_id,
    ).first()
    if not RESULT:
        print("Adding Storm Troopers to manage the Rebels")
        DB_SESSION.add(ADMIN_ROLE)
    DB_SESSION.commit()
except IntegrityError as exp:
    print(exp)
    print("Seems like the roles are added")
except Exception as exp:
    print(exp)
    DB_SESSION.rollback()


def find_record(model, session, filter_dict=None, first_only=True):
    """
    Finds the record by the filter given in a dictionary

    PARAMETERS
    ----------
    model   :   str
        Database table in which the operation takes place
    session    :   sqlalchemy.orm.scoping.scoped_session
        Database session to perform the operation
    filter_dict   :   dict
        Filter dict with column names as keys
        and the intended value as value
    first_only  :   boolean, defaults to True
        Whether to return all the records or only the single
        record (first record if there are multiple matches)

    NOTE
    ---------
    Whilst using no filter_dict and passing first_only
    as false, understand the implications of performance
    """
    records = None
    try:
        if first_only:
            if filter_dict:
                records = session.query(
                    model).filter_by(
                        **filter_dict
                ).first()
            else:
                records = session.query(
                    model
                ).first()
        else:
            if filter_dict:
                records = session.query(
                    model
                ).filter_by(
                    **filter_dict
                ).all()
            else:
                records = session.query(
                    model
                ).all()
    except Exception as exp:
        print(exp)
    return records, session
