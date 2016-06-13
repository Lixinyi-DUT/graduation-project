#coding=utf-8
import scipy.io as sio
from pylab import *
from pylab import mpl
from PIL import Image
import scipy.misc
import math
from numpy import linalg
from scipy.misc import imread
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font=FontProperties(fname=r"c:\\windows\\fonts\\SimSun.ttc", size=14)
data=sio.loadmat('F:\\graduation-project\\codes\\feature_extractor\\data\\results65.mat')
results1=data['results1']
results2=data['results2']
results3=data['results3']
x1=100-results1[:,4]
y1=100-results1[:,5]
c1=results1[:,1]
sv1=results1[:,6]
x2=100-results2[:,4]
y2=100-results2[:,5]
sv2=results2[:,6]
c2=results2[:,1]
r2=results2[:,3]
d2=results2[:,2]
x3=100-results3[:,4]
y3=100-results3[:,5]
sv3=results3[:,6]
c3=results3[:,1]
r3=results3[:,3]
cm = plt.cm.get_cmap('RdYlBu')
cm2 = plt.cm.get_cmap('PiYG')
re1=plt.scatter(x1,y1,marker='s',s=c1*50,c='r',alpha=0.3)
re2=plt.scatter(x2,y2,marker='o',s=c2*50,c=d2,alpha=0.3,cmap=cm)
re3=plt.scatter(x3,y3,marker='^',s=c3*50,c=r3,alpha=0.3,cmap=cm2)
cbar=plt.colorbar(re3)
cb2=plt.colorbar(re2)
plt.xlabel(r'$E_0$(%)')
plt.ylabel(r'$E_1$(%)')
mpl.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus']=False
cb2.set_ticks([2,3,4,5])
cb2.set_label(u'多项式核的次数$d$',labelpad=20,rotation=270,fontsize=14)
cbar.set_ticks([1,2,3,4,5])
cbar.set_ticklabels(['0.01','0.1','1','10','100'])
cbar.set_label(u'RBF核的系数$r$', rotation=270,fontsize=14)
plt.legend((re1,re2,re3),(u'线性核',u'多项式核',u'RBF核'),loc='upper left')
plt.grid(1)

plt.tight_layout()
plt.savefig(r'F:\graduation-project\codes\plots\ill\scatter.png',dpi=100)
plt.savefig(r'F:\graduation-project\presentation\images\scatter.pdf')
plt.show()
