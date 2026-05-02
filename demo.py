from  us_visa.logger import logging 
from us_visa.exception import UsvisaException
import sys

try:
    a=1/0
except Exception as e:
    logging.error("this is error message")
    raise UsvisaException(e,sys)