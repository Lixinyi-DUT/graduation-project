#coding=utf-8
from pylab import *
from PIL import Image
import scipy.misc
from scipy.misc import imread
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

mpl.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus']=False
rcParams["pdf.fonttype"] = 42
font = FontProperties(fname=r"c:\windows\fonts\SimSun.ttc", size=14)
im=imread('F:\\l.png')
im2=imread('F:\\graduation-project\\codes\\output\\stego(gray).png')
im3=imread('F:\\graduation-project\\codes\\output\\stego(gray)2.png')

fig = plt.figure()
ax1 = fig.add_subplot(211)
ax1.hist(im.flatten(),bins=256,alpha=0.3)
plt.xlim([0,255])
plt.xlabel(u'像素值')
plt.ylabel(u'频数')
ax1.set_title(u'(a) 原图像（载体）')
plt.grid(1)

ax2 = fig.add_subplot(212)
ax2.hist(im3.flatten(),bins=256,alpha=0.3,color='g')
plt.xlim([0,255])
plt.xlabel(u'像素值')
plt.ylabel(u'频数')
ax2.set_title(u'(b) 伪装图像')
plt.grid(1)
plt.tight_layout()
plt.savefig(r'F:\graduation-project\codes\plots\ill\hist2.png',dpi=100)
plt.savefig(r'F:\graduation-project\presentation\images\hist2.pdf',dpi=100)
plt.show()
