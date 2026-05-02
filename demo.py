from  us_visa.logger import logging 
from us_visa.exception import UsvisaException
import sys

try:
    a=1/0
    print(a)
except Exception as e:
    raise UsvisaException(e,sys)