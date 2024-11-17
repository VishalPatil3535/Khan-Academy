import logging

class log_maker:
    @staticmethod
    def log_gen():
        logging.basicConfig(filename=".\\Logs\\Khan_Academy.log",format="%(asctime)s:%(levelname)s:%(message)s",
                            datefmt="%y-%m-%d %H:%M:%S",force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger