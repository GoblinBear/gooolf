import logging


class Logger:
    def __init__(self,
                 enable_stream_handler: bool = False,
                 enable_file_handler: bool = False):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        format = logging.Formatter(
            '[%(asctime)s] [%(filename)s: %(lineno)d] [%(levelname)s] %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S')
        
        # Set stream handler
        if enable_stream_handler:
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(logging.DEBUG)
            stream_handler.setFormatter(format)
            self.logger.addHandler(stream_handler)

        # Set file handler
        if enable_file_handler:
            file_handler = logging.FileHandler('log.txt')
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(format)
            self.logger.addHandler(file_handler)

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def error(self, message):
        self.logger.error(message)
