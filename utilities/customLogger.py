import logging
class LogGen:
    @staticmethod
    def loggen(filename="F:/001_Jobs/Python/nopcommerceApp/Logs/test.log", level=logging.INFO):
        logger = logging.getLogger(__name__)
        logger.setLevel(level)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler = logging.FileHandler(filename)
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger
