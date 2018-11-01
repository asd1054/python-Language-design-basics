plaincode = input("请输入明文：")
for p in plaincode:
    #ord()对于数字编码
    #chr（）对应相应的字符
    if ord("a")<=ord(p)<=ord("z"):
        print(chr(ord("a")+ (ord(p)-ord("a") + 3)%26),end='')
    else:
        print(p,end='')
