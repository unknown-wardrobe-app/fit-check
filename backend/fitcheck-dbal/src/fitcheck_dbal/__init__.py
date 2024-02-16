"""
    :module_name: fitcheck_dbal
    :module_summary: A database access layer for the fitcheck backend
    :module_author: Nathan Mendoza
"""

import logging

LOGGER = logging.getLogger(__name__)
LOG_HANDLER = logging.StreamHandler()
LOG_FORMAT = logging.Formatter(
    fmt='[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %z'
)
LOGGER.setLevel(logging.DEBUG)
LOG_HANDLER.setLevel(logging.DEBUG)
LOG_HANDLER.setFormatter(LOG_FORMAT)
LOGGER.addHandler(LOG_HANDLER)
