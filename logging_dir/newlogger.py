import logging
#import basicfile

# logging.basicConfig(filename='new.log', level=logging.DEBUG, format="%(asctime)s %(levelno)s %(name)s")
# instead of using the root logger, lets create our own logger

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# To add a formatter to our user defined logger
formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s")

# configuring file_handler just like the filename in the previous basicConfig
file_handler = logging.FileHandler('newlogger.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
def greet(name):
    return f"Good day {name}"

peace = greet("precious")
logger.info(peace)
