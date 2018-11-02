import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.sans-serif']=['SimHei']
labels = np.array(['综合','KDA','发育','推进','生存','输出'])


nAttr = 6
data = np.array([7,5,6,9,8,7])#数据值
angles = np.linspace(0,2*np.pi,nAttr,endpoint = False)
data = np.concatenate((data,[data[0]]))
angles = np.concatenate((angles,[data[0]]))
fig = plt.figure(facecolor = 'white')
plt.subplot(111,polar = True)
plt.plot(angles,data,'bo-',color ='g',linewidth=2)#BUG
plt.fill(angles,data,facecolor = 'g',alpha=0.25)
plt.thetagrids(angles*180/np.pi,labels)
plt.figtext(0.52,0.95,'DOTA能力值雷达图',ha = 'center')
plt.grid(True)
#plt.savefig('dota_radar.JPG')
plt.show()

#ValueError('x and y must have same first dimension, but have shapes (6,) and (7,)',)

#??还是有问题 只能出现一小部分图片