import logging

"""
in this file, we will log only errors to the file
to do this we will make one more configuration in
line 22
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
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
def greet(name: str):
    try:
        return "You entered the name " + name
    except Exception:
        logger.error("Only string values are allowed in here")

peace = greet(3344)
print(peace)
logger.info(peace)
