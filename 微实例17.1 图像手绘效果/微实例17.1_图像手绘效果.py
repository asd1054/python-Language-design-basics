from PIL import Image
import numpy as np
vec_el = np.pi/2.2  #光源的俯视角度， 弧度值
vec_az = np.pi/4    #光源的方向角度， 弧度值
depth = 10  #(0-100)
im = Image.open('test.jpg').convert('L')
a = np.asarray(im).astype('float')
grad = np.gradient(a)   #图像灰度的梯度值
grad_,grad_y = grad
grad_x *= depth/100
grad_y *= depth/100
dx =  np.cos(vec_el)*np.cos(vec_az) #光源对X轴的影响
dy =  np.cos(vec_el)*np.sin(vec_az) #光源对Y轴的影响
dz =  np.sin(vec_el) #光源对Z轴的影响
A = np.sqrt(grad_x**2+gradgrad_y**2+1.)
uni_x = grad_x/A
uni_y = grad_y/A
uni_z = 1./A
a2 = 255*(dx*uni_x+dy*uni_y+dz*uni_z)   #光源归一化
a2 = a2.clip(0,255)
im2 = Image.fromarray(a2.astype('unit8'))   #重构图像
im2.save('手绘.jpg')

