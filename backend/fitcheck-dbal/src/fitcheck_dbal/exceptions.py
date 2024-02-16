"""
    :module_name: exceptions
    :module_summary: exceptions related to fitcheck database operations
    :module_author: Nathan Mendoza
"""

import logging
from typing import Callable, Mapping, Any
from functools import wraps

LOGGER = logging.getLogger(__name__)


def safe_callback(
    errs: Mapping[Exception, Callable[[Exception, ...], Any]]
) -> Callable[[...], Any]:
    """Isolated exception handling logic decorator
    Args:
        f: the callable object to decorate
        errs: the exception classes to handle and associated callbacks
    Returns:
        decorated callable
    """
    @wraps
    def decorator(f: Callable[[...], Any]) -> Callable[[...], Any]:

        @wraps
        def wrapper(ref, *args):
            try:
                LOGGER.debug("Attempting callback %s", f.__name__)
                result = f(ref, *args)
                LOGGER.debug("Callback succeeded")
                return result
            except Exception as err:
                LOGGER.exception(
                    "Exception occured during callback\n",
                    exc_info=err
                )
                if cb := errs.get(type(err)):
                    LOGGER.debug(
                        "Exception has a responsible callback...calling %s",
                        cb.__name__
                    )
                    return cb(err, *args)
                else:
                    LOGGER.debug(
                        "Exception has no responsible callback...re-raising"
                    )
                    raise err
        return wrapper
    return decorator


class BaseDatabaseAbastractionLayerException:
    """Base exception for the database abstraction layer"""


class NoMatchingDocumentFound(BaseDatabaseAbastractionLayerException):
    """Raised when a query for a document returned no results"""


class NoSuchUser(NoMatchingDocumentFound):
    """Raised when no matching user was found"""
