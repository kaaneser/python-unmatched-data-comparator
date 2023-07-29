import logging

def setup_logger():
    # Created logger instance and set the minimum log level for logger.
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Defined the name of the log file and create a file handler
    log_file = "compare_data.log"
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)

    # Created a console handler for printing log messages
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Created a formatter for customizing log messages
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Added the file and console handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger