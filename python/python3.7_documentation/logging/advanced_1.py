import logging
from random import choice

class ContextFilter(logging.Filter):
    '''
    this is a filter which injects contextual information into the log.
    
    rather than use actual contextual information, we just use random data in this demo
    '''
    
    USERS = ['jim', 'fred', 'sheila']
    IPS = ['123.231.231.123', '127.0.0.1', '192.168.0.1']
    
    def filter(self, record):
        record.ip = choice(ContextFilter.IPS)
        record.user = choice(ContextFilter.USERS)
        return True
    


levels = (logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL)
logging.basicConfig(level=logging.DEBUG,
                   format='%(asctime)-15s %(name)-5s %(levelname)-8s IP:%(ip)-15s User:%(user)-8s %(message)s')
a1 = logging.getLogger('name_1')
a2 = logging.getLogger('name_2')

file = ContextFilter()
a1.addFilter(file)
a2.addFilter(file)
a1.debug('A debug message')
a1.info('An info message with %s','some parameters')
for num in range(10):
    lvl = choice(levels)
    lvlname = logging.getLevelName(lvl)
    a2.log(lvl, 'A message at %s level with %d %s', lvlname, 2, 'parameters')