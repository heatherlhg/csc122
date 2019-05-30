from functools import wraps
import datetime
import logging


def get_logger():
    """
    returns a logging object, if it doesn't exist
    create it, otherwise just return the existing one
    """
    logger = logging.getLogger("trace_logger")

    # if the logger already has 'handlers' just return it.
    if logger.hasHandlers():
        return logger

    # set the logging level (Note we can pass this as a parm)
    logger.setLevel(logging.INFO)

    # create a logging file handler
    fh = logging.FileHandler("trace.log")

    # set the flle handlers format
    fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)

    # add handler to logger object
    logger.addHandler(fh)
    return logger


# decorator function for functions
def trace_function(printArgs=False, printRes=False, log=True):
    def trace(function):
        @wraps(function)
        def do_trace(*args, **kwargs):
            logger = get_logger()

            if log:
                logger.info("Entering {}".format(function.__name__))
                if printArgs:
                    logger.info("<<< Arguments {}".format(args))
            else:
                print("\n[---TRACE---][{0}] Entering {1}".
                      format(datetime.datetime.now(),
                             function.__name__))
                if printArgs:
                    print("[---TRACE---][{0}] Arguments {1}".
                          format(datetime.datetime.now(), args))

            # call the original function    
            res = function(*args, **kwargs)

            if log:
                logger.info("Returning {}".format(function.__name__))
                if printRes:
                    logger.info("<<< Results {}".format(res))
            else:
                print("\n[---TRACE---][{0}] Returning from {1}".
                      format(datetime.datetime.now(), function.__name__))
                if printRes:
                    print("[---TRACE---][{0}] Results {1}".
                          format(datetime.datetime.now(), res))

            #print("\n[---TRACE---] Results {}".format(datetime.datetime.now(), res))

            return res
        return do_trace    
    return trace


# decorator function for class methods
# note the extra self argument passed to the do_trace function
def trace_class_method(printArgs=False, printRes=False, log=True):
    def trace(function):
        @wraps(function)
        def do_trace(self, *args, **kwargs):
            logger = get_logger()

            if log:
                logger.info("Entering {0}.{1}".format(
                         self.__class__.__name__ ,function.__name__))
                if printArgs:
                    logger.info("<<< Arguments {}".format(args))
            else:
                print("\n[---TRACE---][{0}] Entering {1}.{2}".
                      format(datetime.datetime.now(),
                             self.__class__.__name__ ,function.__name__))
                if printArgs:
                    print("\n[---TRACE---][{0}] Arguments {1}".
                          format(datetime.datetime.now(), args))

            res = function(self, *args, **kwargs)

            if log:
                logger.info("Returning {0}.{1}".format(self.__class__.__name__, function.__name__))
                if printRes:
                    logger.info("<<< Results {}".format(res))
            else:
                print("\n[---TRACE---][{0}] Returning from {1}.{2}".
                      format(datetime.datetime.now(),
                             self.__class__.__name__ , function.__name__))
                if printRes:
                    print("\n[---TRACE---][{0}] Results {1}".
                          format(datetime.datetime.now(), res))

            return res
        return do_trace    
    return trace
