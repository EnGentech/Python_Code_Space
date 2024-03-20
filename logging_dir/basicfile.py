import logging

logging.basicConfig(filename='text.log',
                    level=logging.DEBUG, format="%(filename)s %(levelname)s"
                                                "%(asctime)s %(levelno)s %(name)s")
def greet(name):
    return f"Good day {name}"

# The above is a basic logger with root, however its not the best idea, lets dive into
# a better approach to executing logger

'''
since the above logger is executed with the root variable, if the logger is imported
into another function, and the main name space is not defined, the program will run
on import causing the logger to be executed hence its best practice to define your
name, and the best approach to this is using the built in name variable which will
automatically utilize the file name when called.
e.g
'''
 # we assume a file containing a base level of logging have been called

if __name__ == '__main__':
    peace = greet("precious")
    logging.debug(peace)
