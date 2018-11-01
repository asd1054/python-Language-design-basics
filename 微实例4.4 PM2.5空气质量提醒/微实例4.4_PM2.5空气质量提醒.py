PM = eval (input("请输入PM2.5数值："))
if (0<= PM <35):
    print("空气优质，快去户外运动！")
elif 35<=PM <75:
    print("空气良好，适度户外运动！")
elif PM>=75:
    print("空气污染，请小心")
else:
    print("输入有误！")