from wasteDetection.logger import logging

from wasteDetection.exception import AppExceptio
import sys


try:
    a = 3/"s"
except Exception as e:
    raise AppExceptio(e, sys)