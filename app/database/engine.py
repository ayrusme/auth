"""
This file takes care of the engine decalaration
"""

from sqlalchemy import create_engine, event, exc, select
from sqlalchemy.orm import scoped_session, sessionmaker

from config.config import DB_URI
from .schema import (Address, Base, Role, User, UserAuthentication,
                             UserRole)

Session = scoped_session(sessionmaker())

_engine = create_engine(DB_URI, {
    "encoding": "utf-8"
})
try:
    _ = _engine.connect()
except exc.DBAPIError:
    _engine = create_engine(DB_URI, {
    "encoding": "utf-8"
})
Session.remove()
Session.configure(bind=_engine, autoflush=False, expire_on_commit=False)
Base.metadata.create_all(_engine)


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
