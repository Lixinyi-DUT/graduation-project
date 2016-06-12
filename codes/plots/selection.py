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

marker = itertools.cycle(('^', 'v', '8', 's', 'o','h','s'))
line= itertools.cycle(('-','--'))
font=FontProperties(fname=r"c:\\windows\\fonts\\SimSun.ttc", size=14)
data=sio.loadmat('F:\\graduation-project\\codes\\feature_extractor\\data\chi2acc.mat')
