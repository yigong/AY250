import matplotlib.pyplot as plt
import tables as tb
import numpy as np
import pandas as pd

fname = 'electronTrack.h5'
data = tb.openFile(fname)

ntracks = 1111
for i in range(ntracks):
	cmd_track = 'data.root.track.d' + str(i) + '.read()'
	track = eval(cmd_track)[0]

	cmd_Eesc = 'data.root.escape.d' + str(i) + '.read()'
	Eesc = eval(cmd_Eesc)[0][0]



