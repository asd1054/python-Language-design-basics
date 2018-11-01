'''
步骤1：
    请输入带有符号的温度值
步骤2：
    算法
    f=1.8*int(temperature[0,-1])+32
步骤3：
    结果
'''


while 1:
    temperature=input("请输入带有符号的温度值：")
    if temperature[-1] in ["F",'f']:
        c=(eval(temperature[0:-1])-32)/1.8
        print("转换后的温度是：%dC"%c)
    elif temperature[-1] in ['C','c']:
        f=1.8*int(temperature[0:-1])+32
        print("转换后的温度是：%dF"%f)
    elif temperature =="quit()":
        print("正在退出程序")
        #break   
    else:
        print("格式输入错误")
