import logging

"""
This file will log the result into the console
rather than a file, we do this using the streamhandler
"""

#import basicfile

# logging.basicConfig(filename='new.log', level=logging.DEBUG, format="%(asctime)s %(levelno)s %(name)s")
# instead of using the root logger, lets create our own logger

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# To add a formatter to our user defined logger
formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s, %(message)s")

# configuring file_handler just like the filename in the previous basicConfig
file_handler = logging.FileHandler('logError.log')
stream_handler = logging.StreamHandler()
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
stream_handler.setFormatter(formatter)
def greet(name: str):
    try:
        return "You entered the name " + name
    except Exception:
        logger.error("Only string values are allowed in here")

peace = greet(3344)
logger.info(peace)
