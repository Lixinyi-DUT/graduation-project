#coding=utf-8
from pylab import *
import random
import numpy as np
from PIL import Image
import scipy.misc
from scipy.misc import imread
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

def convert_message_to_bit(string_text):
    '''convert the secret message from string to bytearray'''
    bit_string=[]
    for char in string_text:
        bit_string.extend([int(d) for d in bin(char)[2:].zfill(8)])
    return np.array(bit_string)

secret_text=np.random.randint(256, size=48*6)
secret_img=reshape(convert_message_to_bit(secret_text),(48,48))

mpl.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus']=False
rcParams["pdf.fonttype"] = 42
im=imread('F:\\ucid_gray\\00003.png')
h,w=shape(im)
x=np.random.randint(h-48, size=6)
y=np.random.randint(w-48, size=6)

fig = plt.figure()

ax1 = fig.add_subplot(331)
ax1.imshow(im,cmap='gray')
ax1.set_title(u'原图像（载体）')

ax2 = fig.add_subplot(333)
ax2.imshow(im&1,cmap='binary')
ax2.set_title(u'原图像的LSB平面')

subimg1=im[x[0]:x[0]+48,y[0]:y[0]+48]
subimg2=im[x[1]:x[1]+48,y[1]:y[1]+48]
subimg3=im[x[2]:x[2]+48,y[2]:y[2]+48]
subimg4=im[x[3]:x[3]+48,y[3]:y[3]+48]
subimg5=im[x[4]:x[4]+48,y[4]:y[4]+48]
subimg6=im[x[5]:x[5]+48,y[5]:y[5]+48]

ax3 = fig.add_subplot(334)
ax3.imshow(subimg1,cmap='gray')
ax3.set_title(u'位置1')

ax4 = fig.add_subplot(335)
ax4.imshow(subimg2,cmap='gray')
ax4.set_title(u'位置2')

ax5 = fig.add_subplot(336)
ax5.imshow(subimg3,cmap='gray')
ax5.set_title(u'位置3')

ax6 = fig.add_subplot(337)
ax6.imshow(subimg4,cmap='gray')
ax6.set_title(u'位置4')

ax7 = fig.add_subplot(338)
ax7.imshow(subimg5,cmap='gray')
ax7.set_title(u'位置5')

ax8 = fig.add_subplot(339)
ax8.imshow(subimg6,cmap='gray')
ax8.set_title(u'位置6')

plt.show()
