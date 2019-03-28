#!/usr/bin/env python

import threading
import Queue
import time
import os
import operator

# Functions

def read_hkl_file(path_hkl):
    '''Reads a phs file and saves it as a list of lists'''
    array_phs=[]
    file_hkl=open(path_hkl,'r')
    reflections=file_hkl.readlines()
    for i,refle in enumerate(reflections):
        list_values=refle.split() # format: H K L F sigF or H K L I sigI
        h=int(list_values[0])
        k=int(list_values[1])
        l=int(list_values[2])
        f=float(list_values[3])
        sigF=float(list_values[4])
        array_phs.append([h,k,l,f,sigF])
    return array_phs

def sort_reflections_phs(array_refle):
    '''Sorts an array of reflections in ascending order of first h, then k, and then l'''
    array_refle.sort(key=operator.itemgetter(2,1,0))
    return array_refle

def process_hkl_array(array):
    print "Sorting the ",len(array),"reflections"
    sorted_array=sort_reflections_phs(array)
    print "Doing some more useful stuff with my sorted array"
    time.sleep(5)

def worker():
    while True:
        (name_array,array_to_process) = q.get()
        print "\nThread ",threading.current_thread().name, "is processing ",name_array
        process_hkl_array(array_to_process)
        q.task_done()


if __name__ == '__main__':
    q = Queue.Queue()
    for i in range(3):
        t = threading.Thread(target=worker)
        t.daemon = True  
        t.start()
    for fich in os.listdir(os.getcwd()):
        if fich.endswith('.hkl'):
            array_hkl=read_hkl_file(fich)# Read the hkl files and put them into the queue
            q.put((fich,array_hkl))
    q.join()




