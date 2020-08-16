import logging

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

"""
>>> import somelib
>>> somelib.func()  
# no log output 
########
>>> import logging
>>> logging.basicConfig(level=logging.ERROR)
>>> import somelib
>>> somelib.func()  
 critical: somelib a critical error
>>> logging.getLogger('somelib').level=logging.DEBUG
>>> somelib.func()
critical: somelib a critical error
DEBUG: somelib: a debug message
"""


def func():
    log.critical('a critical error')
    log.debug('a debug message')
