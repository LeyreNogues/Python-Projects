#!/usr/bin/env python

import subprocess
                
p1 = subprocess.Popen(["ls","-1"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
p2 = subprocess.Popen(["grep", "example"], stdin=p1.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
p3 = subprocess.Popen(["wc", "-l"], stdin=p2.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = p3.communicate()
print "Found ",int(out)," code examples"



