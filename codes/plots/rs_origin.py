#coding=utf-8
from pylab import *
from PIL import Image
import scipy.misc
from scipy.misc import imread
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font = FontProperties(fname=r"c:\windows\fonts\SimSun.ttc", size=14)
im=imread('F:\\ucid_gray\\00340.png')

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax1.imshow(im,cmap='gray')
ax1.set_title(u'(a) 原图像（载体）',fontproperties=font)

ax1 = fig.add_subplot(122)
ax1.imshow(im&1,cmap='binary')
ax1.set_title(u'(b) LSB平面',fontproperties=font)

plt.show()
