import os
import time
import Queue
import threading
import numpy as np

from folder_watch_thread import WatchThread



class SlowlyFileWriteThread(threading.Thread):
    """
    simulates a slowly write of an image file 
    """
    def __init__(self,dirName, time_to_write = 10., chunksize = 64):
        super(SlowlyFileWriteThread,self).__init__()
        self.dirName = dirName
        self.timestep = 0.1
        self.chunksize = chunksize
        self.nsteps = int(np.ceil(time_to_write/self.timestep))
        self.setDaemon(True)
    

    def run(self):
        """write constantly files to dir"""
        while True:
            fName = os.path.join(self.dirName,"RANDOM_%d.tif"%(time.time()))
            print "writing to %s\n"%fName
            #erase file
            with open(fName,"w") as f:
                pass
            for i in range(self.nsteps):
                with open(fName,"a") as f:
                    f.write("1"*self.chunksize)                
                time.sleep(self.timestep)
            time.sleep(.5)



if __name__ == "__main__":

    dirName =  "tests_watch/"


    
    writeSimulator = SlowlyFileWriteThread(os.path.join(dirName))

    writeSimulator.start()

    
    a = WatchThread(dirName, deltaTime = .1)
    a.start()

    while True:
        try:
            fName = a.goodFiles.get(timeout = 1.)
            print "a new file arrived! ", fName
        except Queue.Empty:
            pass
        time.sleep(.1)

    
