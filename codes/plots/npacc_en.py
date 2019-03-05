#coding=utf-8
import scipy.io as sio
from pylab import *
from PIL import Image
import scipy.misc
import math
from scipy.misc import imread
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import itertools
# mpl.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus']=False
rcParams["pdf.fonttype"] = 42
marker = itertools.cycle(('^', 'v', '8', 's', 'o','h','s'))
line= itertools.cycle(('-','--'))

data=sio.loadmat('F:\\graduation-project\\codes\\feature_extractor\\data\\acc4.mat')
accurancy=data['acc']
em_rate=linspace(5,50,10,endpoint=True);
for i in range(6):
    plt.plot(em_rate,accurancy[i,:],marker = marker.next(),linewidth=2,markersize=10,linestyle=line.next(),label=str(i+1))
plt.xlabel('Embedding rate (%)')
plt.ylabel('Accurancy (%)')
plt.legend(loc='best')
plt.grid(1)
plt.tight_layout()
plt.savefig('F:\graduation-project\codes\plots\ill\\nptest_en.png',dpi=100)
plt.savefig(r'F:\graduation-project\codes\plots\ill\nptest_en.pdf')
plt.show()
