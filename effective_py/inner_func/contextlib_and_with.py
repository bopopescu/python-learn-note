import logging
from contextlib import contextmanager


@contextmanager
def debug_logging(level):
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield
    finally:
        logger.setLevel(old_level)


def my_function():
    logging.debug("Some debug data")
    logging.error("Error log here")
    logging.debug("More debug data")


with debug_logging(logging.DEBUG):
    print("Inside")
    my_function()


@contextmanager
def log_level(level, name):
    logger = logging.getLogger(name)
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield logger
    finally:
        logger.setLevel(old_level)
