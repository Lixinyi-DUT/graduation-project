#coding=utf-8
from pylab import *
from PIL import Image
import scipy.misc
from scipy.misc import imread
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font = FontProperties(fname=r"c:\windows\fonts\SimSun.ttc", size=14)
im=imread('F:\\l.png')
im2=imread('F:\\graduation-project\\codes\\output\\stego(gray).png')
im3=imread('F:\\graduation-project\\codes\\output\\stego(gray)2.png')

fig = plt.figure()

ax1 = fig.add_subplot(221)
ax1.imshow(im,cmap='gray')
ax1.set_title(u'原图像（载体）',fontproperties=font)

ax2 = fig.add_subplot(222)
ax2.imshow(im2,cmap='gray')
ax2.set_title(u'伪装图像',fontproperties=font)

ax3 = fig.add_subplot(223)
ax3.imshow(im&1,cmap='binary')
ax3.set_title(u'原图像（载体）的LSB平面',fontproperties=font)

ax4 = fig.add_subplot(224)
ax4.imshow(im2&1,cmap='binary')
ax4.set_title(u'伪装图像的LSB平面',fontproperties=font)

plt.tight_layout()
plt.savefig('F:\graduation-project\codes\plots\ill\lsb_plane_comp.png',dpi=100)

plt.show()
