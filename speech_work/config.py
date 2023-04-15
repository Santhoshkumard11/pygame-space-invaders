import logging
import sys
import coloredlogs


def set_logger():
    log_handler = logging.StreamHandler(sys.stdout)
    str_fmt = "%(asctime)s | %(module)s | line %(lineno)d | %(levelname)s | %(message)s"
    formatter = logging.Formatter(str_fmt)
    log_handler.setFormatter(formatter)

    coloredlogs.install(level=logging.INFO, handlers=[log_handler], fmt=str_fmt)
