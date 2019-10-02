## DL  - Downloader for Linux Terminal

##### Beta release

* Much faster than regular downloaders [Tested].

* CLI Knowledge rquire , but simple to use.

* Program works under python 3+ ( May not be work > 2.x)


Principle
---------

For regular download we use curl or wget . These programs support threads but for newbies its very hard to calculate and use it. In this program i used curl as backend.
While you download , downloader split your target file to multiple chunks and calculate its bytes and directly download from that stream. 

Example :   `dl http://www.example.com/os.iso 10`

This command will download os.iso using 10 threads. Each 10 threads download a range of data from the source and merge together. 

Installation
------------

* Clone repository to your system

`git clone https://github.com/jamesarems/dl.git`

* Move program file to system binary

`cd dl ; mv dl.py /usr/bin/dl`


Thats it!



