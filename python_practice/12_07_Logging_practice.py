"""
# # Author Anilkumar
# # problem Statement:
# # input :
   output :
"""

#importing module
import logging


logging.basicConfig()

#creating an object
logger=logging.getLogger()


#setting the threshold of logger to DEBUG
logger.setLevel(logging.ERROR)

#Test messages
logger.debug("Harmless debug message")
logger.info("Just an information")
logger.warning("Its a warning")
logger.error("Did you try to divide by zero")
logger.critical("Internet is down")