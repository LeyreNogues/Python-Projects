#!/usr/bin/env python

import threading
import random
import time

class ABManager:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.lock = threading.Lock()

    def changeA(self):
        if not self.lock.locked():
            print "Lock acquired"
            self.lock.acquire()
        print "Thread ",(threading.currentThread()).name," is changing A"
        self.a = self.a + 1
        if self.lock.locked():
            self.lock.release()
            print "Lock released"

    def changeB(self):
        if not self.lock.locked():
            print "Lock acquired"
            self.lock.acquire()
        print "Thread ",(threading.currentThread()).name," is changing B"
        self.b = self.b + self.a
        if self.lock.locked():
            self.lock.release()
            print "Lock released"

    def changeAandB(self):
        if not self.lock.locked():
            print "Lock acquired"
            self.lock.acquire()            
        print "Thread ",(threading.currentThread()).name," is changing A and B"
        self.changeA() 
        self.changeB()
        if self.lock.locked():
            self.lock.release()
            print "Lock released"

def worker(managerAB):
    r = random.random()
    time.sleep(r)
    if 0.5 < r < 1.0:
        managerAB.changeAandB()
    elif 0.3 < r < 0.5:
        managerAB.changeA()
    else:
        managerAB.changeB()     

if __name__ == '__main__':
    manager = ABManager()
    for i in range(10):
        t = threading.Thread(target=worker,args=(manager,))
        t.start()
    main_thread = threading.currentThread()
    for t in threading.enumerate():
        if t is not main_thread:
            t.join()


