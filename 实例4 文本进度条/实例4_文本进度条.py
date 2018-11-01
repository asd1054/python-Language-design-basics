#简单的开始
#import time 
#scale = 10
#print("{0:-^20}".format("执行开始"))
#for i in range(scale +1):
#    a,b = '**' * i,'..'*(scale - i)
#    c = (i/scale)*100
#    print("%{:^3.0f}[{}->{}]".format(c,a,b))
#    time.sleep(0.1)
#print("执行结束".center(20,'-'))

#单行动态刷新
#import time
#for i in range (101):
#    print("\r{:2}%".format(i),end='')
#    time.sleep(0.05)
#print('')


#带刷新的文本进度条
import time
scale = 50
print("{0:-^50}".format("执行开始"))
t = time.clock()
for i in range(scale +1):
    a,b = '**' * i,'..'*(scale - i)
    c = (i/scale)*100
    t -= time.clock()
    print("\r%{:^3.0f}[{}->{}]{:.2f}s".format(c,a,b,-t),end='')
    time.sleep(0.05)
print('')
print("执行结束".center(50,'-'))