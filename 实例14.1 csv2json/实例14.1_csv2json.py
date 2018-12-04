
import json
fr = open('price2016.csv','r')
ls = [] 
for line in fr :
    line = line.replace('\n','')
    ls.append(line.split(','))
fr.close()
fw = open('price2016.json','w')
lt = ls.copy()
for i in range(1,len(lt)):
    lt[i] = dict(zip(lt[0],lt[i]))
json.dump(lt[1:],fw,sort_keys = True,indent = 4)
fw.close()