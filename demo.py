from  us_visa.logger import logging 
from us_visa.exception import UsvisaException
import sys

try:
    logging.info("Demo ran successfully")
    print("Demo ran successfully")
except Exception as e:
    raise UsvisaException(e,sys)
