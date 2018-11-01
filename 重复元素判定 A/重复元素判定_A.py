
'''
描述

接收用户输入的一个列表，如果列表中元素存在重复，则返回True，否则返回False。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬ 
'''

li = list(input())
se = set(li)
a = len(li)
b = len(se)
if a!=b:
    print("True")
else:
    print("False")