def to_dict(fname):
	import tables as tb
	import numpy as np
	import pandas as pd
	import cPickle as pickle
	from collections import OrderedDict 

	data = tb.openFile(fname)
	cmd_0 = 'data.root.'
	event = OrderedDict()
	for i in xrange(254534):
		cmd_track = cmd_0 + 'track.d' + str(i) + '.read()'
		cmd_escape = cmd_0 + 'Eesc.d' + str(i) + '.read()'
		track = eval(cmd_track)[0]
		escape = eval(cmd_escape)[0]
		event['d'+str(i)] = [track, escape[0]]
	event
	pickle.dump(event, open('event_200k.pkl', 'wb'))
	return event