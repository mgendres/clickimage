#!/usr/bin/python
# This is a simple program that will allow one to click on an image and record the pixel locations
import sys
import os.path
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import copy as copy
import numpy as np

if len(sys.argv)!=2:
  print('Usage: '+sys.argv[0]+' <png filename>')
  exit()

img_file=sys.argv[1]
if not os.path.exists(img_file):
  print('Image file does not exist!')
  exit()

img0 = mpimg.imread( img_file )
img = copy.deepcopy(img0)
print img.shape

fig = plt.figure()
myobj = plt.imshow(img, interpolation='nearest')

def Complement(rgb):
  comp = np.ones(len(rgb), dtype=int) - rgb
  if len(comp)==4:
    comp[-1] = 1
#  comp = [0,0,0,1]
  return comp

# Actions taken upon click
coords = []
def onclick(event):
  if event.dblclick:
    i, j = event.xdata, event.ydata # get pixels
    i += 0.5
    j += 0.5
    print '%f, %f'%(i, j)
    u = int(i)
    v = int(j)
    coords.append( (u, v) ) # record pixels
    img[ v, u ] = Complement( img0[ v, u ] )
    if (1):
      for s in [-3, -2, -1, 1, 2, 3]:
        img[ v+s, u ] = Complement( img0[ v+s, u ] )
        img[ v, u+s ] = Complement( img0[ v, u+s ] )
    if (0):
      for s in range(-3,4):
        for t in range(-3,4):
          img[ v+s, u+t ] = Complement( img0[ v+s, u+t ] )
      for coord in coords:
        u,v=coord
        img[v,u]=img0[ v, u ]
    myobj.set_data(img) # update image data
    plt.draw() # redraw image

fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()

print "Pixels selected:"
print list(set(coords))
