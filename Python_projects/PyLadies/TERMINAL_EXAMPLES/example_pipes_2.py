#!/usr/bin/env python

import multiprocessing
import time

def consumer(p1,p2):
    p1.close()
    while True:
        try:
            item = p2.recv()
        except EOFError:
            break
        print '\nConsuming ',item # do something with item

def producer(sequence, output_p):
    for item in sequence:
        print '\nSending ',item
        time.sleep(2)
        output_p.send(item)

                
if __name__ == '__main__':
 
    p1, p2 = multiprocessing.Pipe() # Returns the two ends of a pipe 
 	
    cons = multiprocessing.Process(target=consumer,args=(p1,p2))
    cons.start()
 	
    p2.close() 
    
    # Produce some data
    sequence = xrange(100) 
    producer(sequence, p1)

    p1.close() # Close the output end


