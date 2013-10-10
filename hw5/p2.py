# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 16:42:45 2013

@author: Yigong
"""
"""PyAudio Example: Play a WAVE file."""
import sys
import wave
import pyaudio
import aifc
import numpy as np
import matplotlib.pyplot as plt
import numpy.fft as fft
from numpy.fft import fftshift
CHUNK = 1024
if len(sys.argv) < 2:
    print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
    sys.exit(-1)

wf = wave.open(sys.argv[1], 'rb')
p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)
RATE = wf.getframerate()
data = wf.readframes(CHUNK)
all_data = []
while data != '':
    all_data.append(data)    
    stream.write(data)
    data = wf.readframes(CHUNK)
    
stream.stop_stream()
stream.close()
p.terminate()
data = "".join(all_data)
integer_data = np.fromstring(data, dtype=np.int32)
time = np.arange(len(integer_data)) / float(RATE)

fig1, [ax0, ax1] = plt.subplots(2,1)
ax0.plot(time, integer_data, color='b', linestyle='-')
plot_title_1 = ('sound waveform')
ax0.set_xlabel("Time [s]")
ax0.set_ylabel("Amplitude")
ax0.set_xlim(min(time), max(time))
ax0.set_title(plot_title_1)

power = (fft.fft(fftshift(integer_data)))
half = len(power)/2
freq = np.linspace(0,RATE,len(power))
power = power[0:half]
power = 10*np.log10((abs(power))**2)
freq = freq[0:half]
ax1.plot(freq, power, c = 'r')
plot_title_2 = ('Frequency spectrum')
ax1.set_xlabel("Freq [Hz]")
ax1.set_ylabel("Power [dB]")
ax1.set_xlim(min(freq), max(freq))
ax1.set_title(plot_title_2)




plt.show()



