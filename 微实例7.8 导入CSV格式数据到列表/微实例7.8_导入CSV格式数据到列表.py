fo = open('test.csv','r')
ls =[]
for line in fo :
    line = line.replace('\n','')
    ls.append(line.split(','))
print(ls)
