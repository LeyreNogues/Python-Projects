#!/usr/bin/env python

import time
import threading
import logging

logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-9s) %(message)s',)

def n():
    logging.debug('Starting')
    logging.debug('Exiting')

def d():
    logging.debug('Starting')
    time.sleep(5)
    logging.debug('Exiting')

if __name__ == '__main__':

     t = threading.Thread(name='non-daemon', target=n)

     d = threading.Thread(name='daemon', target=d)
     d.setDaemon(True)

     t.start()
     d.start()
    
     t.join()
     
     print 'Here is my interesting next part of the code' 
