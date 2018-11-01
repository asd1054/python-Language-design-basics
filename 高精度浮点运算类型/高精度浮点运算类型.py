while 1:
    print("请输入两个高精度浮点数")
    a=input("第一个：")
    if a=="quit()":
        break
    a=float(a)
    b=input("第二个：")
    if b=="quit()":
        break
    b=float(b)
    print("1：加法")
    print("2：减法")
    print("3：乘法")
    print("4：除法")
    c=input("请输入要运算的类型：")
    if c=="quit()":
        break
    c=int(c)
    if c==1:
        print(a+b)
    elif c==2:
        print(a-b)
    elif c==3:
        print(a*b)
    elif c==4:
        print(a/b)
    else:
        print("输入异常！！！请重新输入")

