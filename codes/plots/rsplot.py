#coding=utf-8
import scipy.io as sio
from pylab import *
from PIL import Image
import scipy.misc
from scipy.misc import imread
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

mpl.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus']=False
rcParams["pdf.fonttype"] = 42
font=FontProperties(fname=r"c:\\windows\\fonts\\SimSun.ttc", size=14)
data=sio.loadmat('F:\\graduation-project\\codes\\feature_extractor\\data\\rsdata.mat')
RSU_FM=data['RSU_FM']
RSU_M=data['RSU_M']

R_FM=RSU_FM[:,0]
S_FM=RSU_FM[:,1]
R_M=RSU_M[:,0]
S_M=RSU_M[:,1]
X=linspace(0,100,11,endpoint=True);
plt.plot(X,R_FM,label=r'$R_{-M}$',linestyle='--',marker='o',color='red',linewidth=1.5)
plt.plot(X,R_M,label=r'$R_M$',linestyle='-',color='red',marker='s',linewidth=1.5)
plt.plot(X,S_FM,label=r'$S_{-M}$',linestyle='--',color='blue',marker='D',linewidth=1.5)
plt.plot(X,S_M,label=r'$S_M$',linestyle='-',color='blue',marker='^',linewidth=1.5)
plt.grid(1)
plt.legend(loc=0)
plt.xlabel(u'隐写率（%）')
plt.ylabel(u'组数')
plt.tight_layout()
plt.savefig(r'F:\graduation-project\codes\plots\ill\rsdemo.png',dpi=100)
plt.savefig(r'F:\graduation-project\presentation\images\rsdemo.pdf')
plt.show()
