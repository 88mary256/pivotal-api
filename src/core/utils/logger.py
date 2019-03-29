import logging
class LoggerTodoly:

    def __init__(self):
        logging.basicConfig(level=logging.DEBUG)
        logging.getLogger(__name__)