#!/usr/bin/python
## License OpenSource
## Author : James PS
## This is an attempt to introduce new fast downloaded for Unix system
##
import os, subprocess, sys
from os.path import basename
import timeit

try:
    filename = basename(sys.argv[1])
    tr = int(sys.argv[2])
except IndexError:
    print('Wrong parameters, eg: dl <download-link> <thread-count>')
    exit(1)

def calc():
    try:
        CMD1 = "curl -Is %s | grep Content-Length | awk '{print $2}' " % (sys.argv[1])
        os.system('clear')
        size = os.popen(CMD1).read()
        print('File Size : ', size)
        print('File Name : ', filename)
        value = int(int(size) / int(sys.argv[2]))
        thread(value)
    except IndexError:
        print('Wrong parameters, eg: dl <download-link> <thread-count>')
        exit(1)
def thread(value):
    count = 0
    rval = value
    rsize = []
    for i in range(tr):
        rfile = "."+filename+"."+str(i)
        if ( i == (int(tr) - 1)):
            shot1 = "curl -s -o %s --range %s- %s & " % (rfile, count, sys.argv[1])
            rsize.append(shot1)
        shot1 = "curl -s -o %s --range %s-%s %s & " % (rfile, count, rval, sys.argv[1])
        rsize.append(shot1)
        count = rval + 1
        rval = int(int(rval) + int(value))
    dload(rsize,tr)

def dload(rsize,tr):
    cmd1 = "cat .%s.? > %s ; rm -rf .%s.* ; rm -rf .dlt.sh" % (filename, filename, filename)
    for i in range(tr):
        cmd2 = "echo '%s' >> .dlt.sh" % (rsize[i])
        os.system(cmd2)
    print('Download in progress..')
    os.system('echo wait >> .dlt.sh ; chmod +x .dlt.sh')
    try:
        start = timeit.default_timer()
        subprocess.call('./.dlt.sh', shell=True)
        os.system(cmd1)
        stop = timeit.default_timer()
        print('Completed in ', stop - start)
    except KeyboardInterrupt:
        os.system('pkill curl ; rm -rf .dlt.sh; rm -rf .%s.*' % (filename))
        print('Cancel request accepted [OK]')


calc()

