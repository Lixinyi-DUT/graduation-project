#coding=utf-8
import scipy.io as sio
from pylab import *
from PIL import Image
import scipy.misc
from scipy.misc import imread
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font=FontProperties(fname=r"c:\\windows\\fonts\\SimSun.ttc", size=14)
data=sio.loadmat('F:\\graduation-project\\codes\\feature_extractor\\data\\rsdata.mat')
RSU_FM=data['RSU_FM']
RSU_M=data['RSU_M']

R_FM=RSU_FM[:,1]
S_FM=RSU_FM[:,2]
R_M=RSU_M[:,1]
S_M=RSU_M[:,2]
X=linspace(0,100,11,endpoint=True);
plt.plot(X,R_FM,label=r'$R_{-M}$')
plt.plot(X,R_M,label=r'$R_{M}$')
plt.plot(X,S_FM,label=r'$S_{-M}$')
plt.plot(X,S_M,label=r'$S_{M}$')
plt.legend(loc='upper right')
plt.show()
print(RSU_M[:,1])
