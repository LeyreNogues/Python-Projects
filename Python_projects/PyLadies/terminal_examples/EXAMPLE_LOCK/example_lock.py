#!/usr/bin/env python
import threading
import time
import logging
import os
import re

# Define function to read shelxe output
def extract_best_CC_shelxe(complete_output):
    """Given the contents of an lst file (output from shelxe), it will look for the value of the final best value of CC"""
    lines=complete_output.split("\n")
    regexCC=re.compile('Best trace')
    for i,_ in enumerate(lines):
            if bool(regexCC.findall(lines[i])):
                cut_first=lines[i].split("%")[0]
                CC=float(cut_first.split()[6])
                return CC
# Start logging
logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-9s) %(message)s',)
                    
class BestSolution(object):
    def __init__(self):
        self.cc = 0
    def setCCvalue(self,cc_value):
        self.cc = cc_value

def worker(best,solution):
    logging.debug('Launching shelxe job ........ ')
    time.sleep(10)
    solution_file=open(solution,'r')
    solution_content=solution_file.read()
    cc_from_solution=extract_best_CC_shelxe(solution_content)
    logging.debug('CC read from solution '+str(cc_from_solution))
    lock.acquire()
    logging.debug('Acquire the lock')
    if cc_from_solution>best.cc:
        logging.debug('New best CC found, saving it to BestSolution '+str(cc_from_solution)) 
        best.setCCvalue(cc_from_solution)
    lock.release()
    logging.debug('Release the lock')

if __name__ == '__main__':
    best = BestSolution()
    lock=threading.Lock()
    list_files=os.listdir(os.getcwd())
    for fich in list_files:
        if fich.endswith('.lst'):
            solution=fich
            t = threading.Thread(target=worker, args=(best,solution,))
            t.start()

    logging.debug('Waiting for worker threads....')
    main_thread = threading.currentThread()
    for t in threading.enumerate():
        if t is not main_thread:
            t.join()
    logging.debug('Maximum final CC value found is '+str(best.cc))



