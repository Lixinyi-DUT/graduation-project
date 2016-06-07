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
plt.xlim([0,255])
#plt.hist(im.flatten(),bins=256,alpha=0.3,label='cover')
plt.hist(im3.flatten(),bins=256,alpha=0.3)
plt.xlabel(u'像素值',fontproperties=font)
plt.ylabel(u'频数',fontproperties=font)
#plt.title(u'伪装图像的像素值直方图',fontproperties=font)
plt.grid(1)
plt.tight_layout()
plt.savefig('F:\graduation-project\codes\plots\ill\hist_stego.png',dpi=75)
#plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig(r'F:\graduation-project\codes\plots\ill\hist.png',dpi=100)

plt.show()
#print(im.flatten())
