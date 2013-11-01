import urllib
import urllib2
import simplejson
import matplotlib, sys
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.misc import imread
import matplotlib.pyplot as plt
from Tkinter import *
import skimage.filter as filter
import numpy as np
from scipy.misc import imfilter
import skimage
from skimage.morphology import disk

def image_mani(image_array, mani):
    return imfilter(image_array, mani)
    
def refresh_func():
    new_image = imgLF.image 
    ax1.imshow(new_image, cmap=plt.cm.gray)
    canvas.show()

def blur_func():
    new_image = image_mani(imgLF.image, 'blur')
    ax1.imshow(new_image, cmap=plt.cm.gray)
    canvas.show()

def sharpen_func():
    new_image = image_mani(imgLF.image, 'sharpen')
    ax1.imshow(new_image, cmap=plt.cm.gray)
    canvas.show()
    
def smooth_func():
    new_image = image_mani(imgLF.image, 'smooth')
    ax1.imshow(new_image, cmap=plt.cm.gray)
    canvas.show()
    
def edge_func():
    new_image = image_mani(imgLF.image, 'edge_enhance')
    ax1.imshow(new_image, cmap=plt.cm.gray)
    canvas.show()
    
#def contrast_func():
#    new_image = skimage.filter.rank.morph_contr_enh(imgLF.image.astype(np.uint8), disk(20))
#    ax1.imshow(new_image, cmap=plt.cm.gray)
#    canvas.show()
    
def color_func():
    new_image = imgLF.image_clr
    ax1.imshow(new_image)
    canvas.show()

def decolor_func():
    new_image = imgLF.image 
    ax1.imshow(new_image, cmap=plt.cm.gray)
    canvas.show()
    
def brighten_func():
    new_image = imgLF.image*10
    ax1.imshow(new_image, cmap=plt.cm.gray)
    canvas.show()

def darken_func():
    new_image = imgLF.image*0.5
    ax1.imshow(new_image, cmap=plt.cm.gray)
    canvas.show()

def exit_func():
    master.destroy()
    exit()

def searchPic():
    searchTerm = kwords.get()
    searchTerm = searchTerm.replace(' ','%20')
    url = ('https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=' +
           searchTerm+ '&userip=INSERT-USER-IP')
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)    
    # Process the JSON string.
    results = simplejson.load(response)
    imgURL = results['responseData']['results'][0]['unescapedUrl']
    imgName = imgURL.split('/')[-1]
    img_temp = urllib.URLopener().retrieve(imgURL, imgName)
    img_array = imread(img_temp[0])
    url_label.config(text=imgURL)
    
    imgLF.image = imread(imgName, flatten=True)
    imgLF.image_clr = imread(imgName)
    ax1.imshow(imgLF.image, cmap=plt.cm.gray)
    canvas.show()
    
    refresh.config(state=NORMAL, command=refresh_func)
    blur.config(state=NORMAL, command=blur_func)
    sharpen.config(state=NORMAL, command=sharpen_func)
    smooth.config(state=NORMAL, command=smooth_func)
    edge.config(state=NORMAL, command=edge_func)
    #contrast.config(state=NORMAL, command=contrast_func)
    color.config(state=NORMAL, command=color_func)
    decolor.config(state=NORMAL, command=decolor_func)
    brighten.config(state=NORMAL, command=brighten_func)
    darken.config(state=NORMAL, command=darken_func)
    
    
master = Tk()

inputLF = LabelFrame(master, text='Input', padx=10, pady=10)
inputLF.pack(fill=BOTH, expand=1)
input_label = Label(inputLF, text='Query string:')
input_label.pack(side=LEFT)
kwords = Entry(inputLF)
kwords.pack(side=LEFT)
run_button = Button(inputLF, text='Run query', command=searchPic)
run_button.pack(side=LEFT)

urlLF = LabelFrame(master, text='Image URL', padx=10, pady=10)
urlLF.pack(fill=BOTH, expand=1)
url_label = Label(urlLF, text=' ')
url_label.pack(fill=BOTH, expand=1)

imgLF = LabelFrame(master, text='Image Display', padx=10, pady=10)
imgLF.pack(fill=BOTH, expand=1)
f1, ax1 = plt.subplots()
ax1.spines['left'].set_color('none')
ax1.spines['right'].set_color('none')
ax1.spines['top'].set_color('none')
ax1.spines['bottom'].set_color('none')
ax1.set_xticks([])
ax1.set_yticks([])
canvas = FigureCanvasTkAgg(f1, master=imgLF)
canvas.show()
canvas.get_tk_widget().pack(fill=BOTH, expand=1)

maniLF = LabelFrame(master, text='Image Manipulations Options', padx=10, pady=10)
maniLF.pack(fill=BOTH, expand=1)
refresh = Button(maniLF, text='Refresh', state=DISABLED)
refresh.pack(side=LEFT)
blur = Button(maniLF, text='Blur', state=DISABLED)
blur.pack(side=LEFT)
sharpen = Button(maniLF, text='Sharpen', state=DISABLED)
sharpen.pack(side=LEFT)
smooth = Button(maniLF, text='Smooth', state=DISABLED)
smooth.pack(side=LEFT)
edge = Button(maniLF, text='Edge', state=DISABLED)
edge.pack(side=LEFT)
#contrast = Button(maniLF, text='Contrast', state=DISABLED)
#contrast.pack(side=LEFT)
color = Button(maniLF, text='Color', state=DISABLED)
color.pack(side=LEFT)
decolor = Button(maniLF, text='Decolor', state=DISABLED)
decolor.pack(side=LEFT)
brighten = Button(maniLF, text='Brighten', state=DISABLED)
brighten.pack(side=LEFT)
darken = Button(maniLF, text='Darken', state=DISABLED)
darken.pack(side=LEFT)


qt = LabelFrame(master,text='')
qt.pack(fill=BOTH, expand=1)
qt_bt= Button(qt, text='OK', command=exit_func)
qt_bt.pack(side=RIGHT)

master.mainloop()