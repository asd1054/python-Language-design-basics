data = {0:'ling',1:'yi',2:'er',3:'san',4:'si',5:'wu',6:'liu',7:'qi',8:'ba',9:'jiu'}
a = input()
if a[0] == '-':
    print('fu',end = ' ')
    a = a[1:]
l = len(a)
cnt=0
for i in a:
    cnt +=1
    i = int(i)
    if cnt ==l:
        print(data[i])
        break
    print(data[i],end = ' ')
