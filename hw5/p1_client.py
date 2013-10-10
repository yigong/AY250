"""
Created on Mon Oct  7 21:37:51 2013

@author: Yigong
"""
from scipy.misc import *
import xmlrpclib
import matplotlib.pyplot as plt
import numpy as np

host, port = 'localhost', 5054
proxy = xmlrpclib.ServerProxy('http://%s:%d' %(host, port), allow_none=True)
img_array = imread('airplanes_0015.jpg', flatten=False)
img_array = img_array[100:150, 100:150, :]
img_list = img_array.tolist()

mani_list = proxy.flipUD(img_list)
mani_array = np.array(mani_list)
f1, [ax0, ax1] = plt.subplots(1,2)
ax0.imshow(img_array)
ax1.imshow(mani_array)
imsave('client_original.png', img_array)
imsave('client_manipulated.png', mani_array)