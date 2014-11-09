
import numpy as np
import time

import pyclearvolume

print "creating the server"

d = pyclearvolume.DataServer(maxVolumeNumber=2)

print "starting the server"

d.start()

time.sleep(1)

print "starting to serve data"

N = 128
data = np.linspace(0,65000,N**3).reshape((N,)*3).astype(np.uint16)

t = 0
while True:
    args = {}
    args["color"] = "%s %s %s 1."%tuple([str(c) for c in np.random.uniform(0,1,3)])
    args["voxelwidth"] = np.random.uniform(.2,1.6)
    args["voxelheight"] = np.random.uniform(.2,1.6)
    args["voxeldepth"] = np.random.uniform(.2,1.6)
    args["time"] = t

    print "sending..."
    print args
    d.sendData(data,**args)
    # d.sendData(data)
    time.sleep(2)
    t += 1