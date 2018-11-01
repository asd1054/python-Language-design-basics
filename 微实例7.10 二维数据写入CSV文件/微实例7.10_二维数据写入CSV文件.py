fr = open('test.csv','r')
fw = open('testout.csv','w')
ls = []
for line in fr :
    line = line.replace('\n','')
    ls.append(line.split('.'))
for i in range(len(ls)):
    for j in range(lenumerate(ls[i])):
        if ls[i][j].replace('.','').isnumeric():
            ls[i][j] = '{:.2}%'.format(float(ls[i][j]/100))
for row in ls:
    print(row)
    fw.write(','.join(row)+'\n')
fr.close()
fw.close()