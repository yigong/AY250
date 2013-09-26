import numpy as np
import matplotlib.pyplot as plt
tp = [('date','i8'),('value','f8')]
yahoo_data = np.loadtxt('yahoo_data.txt',dtype=tp, skiprows=1)
google_data = np.loadtxt('google_data.txt',dtype=tp, skiprows=1)
ny_data = np.loadtxt('ny_temps.txt',dtype=tp, skiprows=1)
f0, ax0 = plt.subplots()
ax2 = ax0.twinx()
yahoo_line = ax0.plot(yahoo_data['date'], yahoo_data['value'], color = 'm', label = 'Yahoo! Stock Value',linewidth = 1.5)
google_line = ax0.plot(google_data['date'], google_data['value'], color = 'b', label = 'Google Stock Value', linewidth = 1.5)
ny_line = ax2.plot(ny_data['date'], ny_data['value'], color = 'r', label = 'NY Mon. High Temp', linestyle = '--', linewidth = 1.5)
lines = yahoo_line+google_line+ny_line
labels = [l.get_label() for l in lines]
ax0.legend(lines,labels, 'center left',fontsize = 'medium', frameon = False)
ax0.set_ylim(-20,780)
ax0.set_xlim(48800,55600)
ax0.set_ylabel('Value (Dollars)', fontsize = 'large')
ax0.set_xlabel('Date (MJD)', fontsize = 'large')
ax0.set_title('New York Temperature, Google, and Yahoo!', fontsize ='x-large')
ax2.set_ylim(-150,100)
ax2.set_ylabel('Temperature ($^\circ$F)', fontsize = 'large')
plt.show()