import logging

from src.core.utils.property_reader import PropertyReader


class logger_pivotal:

    def __init__(self):
        logging.basicConfig(level=logging.DEBUG)
        self.log = logging.getLogger(__name__)
        self.config = PropertyReader()
        handler = logging.FileHandler(self.config.get_logger_path())

        formatter = logging.Formatter(self.config.get_logger_format())
        handler.setFormatter(formatter)

        self.log.addHandler(handler)

    def set_info(self, message):
        self.log.info(message)

    def set_debug(self, message):
        self.log.debug(message)

    def set_error(self, message):
        self.log.error(message)

    def set_exception(self, message):
        self.log.exception(message)
