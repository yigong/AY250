import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
tp = [('sepalL','f8'),('sepalW','f8'),('petalL','f8'),('petalW','f8'),('species','S10')]
flower_data = np.loadtxt(open('flowers.csv','rb'),dtype=tp, skiprows=1, delimiter=',')
ctable = dict(setosa = 'r', versicolor = 'g', virginica = 'b')
carray = [ctable[x] for x in flower_data['species'] ]

class BrushingRectangle:
    def __init__(self,ax):
        self.rect = None
        self.press = False
        self.ax = ax
        self.cidpresss = self.ax.figure.canvas.mpl_connect('button_press_event', self.on_press)
        self.cidrelease = self.ax.figure.canvas.mpl_connect('button_release_event', self.on_release)
        self.x0 = None
        self.x1 = None
        self.y0 = None
        self.y1 = None
    def on_press(self, event):
        xp = event.x
        yp = event.y
        self.press = True
        self.x0 = xp
        self.y0 = yp
        print 'press at', xp, yp

        
    def on_release(self, event):
        self.xl = event.x
        self.yl = event.y
        print 'release at', self.xl, self.yl
        x_ll = min(self.x0, self.x1)
        y_ll = min(self.y0, self.y1)
        width = abs(self.x0- self.x1)
        height = abs(self.y0- self.y1)
        print x_ll, y_ll, width, height
        self.ax.add_patch(self.rect)
        self.rect.set_xy((x_ll,y_ll))
        self.rect.set_width(width)
        self.rect.set_height(height)
        
        self.ax.figure.canvas.draw()
        self.press = False
        
    def disconnect(self):
        self.ax.figure.canvas.mpl_disconnect(self.cidpresss)
        self.ax.figure.canvas.mpl_disconnect(self.cidrelease)
    
features = ['sepalL','sepalW','petalL','petalW']
f0, axx = plt.subplots(4,4, figsize = (12,8))

for i, row in enumerate(features):
    for j, col in enumerate(features):
        axx[j][i].scatter(flower_data[row], flower_data[col],alpha=0.5,s = 30, c=carray, edgecolors = 'none')
        brush = BrushingRectangle(axx[j][i])
plt.show()