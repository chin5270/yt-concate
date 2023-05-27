import logging


def config_logging(logging_level):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    file_name = 'yt_concate.log'
    formatter = logging.Formatter('%(asctime)s : %(name)s : %(levelname)s : %(message)s')

    file_handler = logging.FileHandler(file_name)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging_level)
    logger.addHandler(stream_handler)