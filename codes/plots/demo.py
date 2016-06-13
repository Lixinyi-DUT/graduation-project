#coding=utf-8
from pylab import *
from PIL import Image
import scipy.misc
from scipy.misc import imread
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

mpl.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus']=False
im=imread('F:\\l.png')

fig = plt.figure()

ax1 = fig.add_subplot(121)
ax1.imshow(im,cmap='gray')
ax1.set_title(u'(a) 原图像（载体）')

ax1 = fig.add_subplot(122)
ax1.imshow(im&254,cmap='gray')
ax1.set_title(u'(b) 去掉LSB位后的图像')

plt.tight_layout()
plt.savefig('F:\graduation-project\codes\plots\ill\demo1.png',dpi=100)
plt.savefig('F:\graduation-project\codes\plots\ill\demo1.pdf')

plt.show()
