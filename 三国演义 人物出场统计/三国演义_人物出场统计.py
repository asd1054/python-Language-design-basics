import jieba 
excludes= {"将军","却说","荆州","二人","不可","不能","如此",'商议','如何','主公','左右','于是','东吴','引兵','军马','军士','都督','陛下','一人','不敢','人马','不知','次日','大喜','魏兵','天下','汉中','只见','众将','蜀兵','今日','后主','大叫','太守','此人','夫人','上马'}
txt = open("三国演义.txt","r",encoding = "utf-8").read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word =="诸葛亮" or word == "孔明曰":
        rword = "孔明"
    elif word =="关公" or word == "云长":
        rword = "关羽"
    elif word =="玄德" or word == "玄德曰":
        rword = "刘备"
    elif word =="孟德" or word == "丞相":
        rword = "曹操"
    else:
        rword = word 
    counts[rword]=counts.get(rword,0)+1
for word in excludes:
    del(counts[word])
items = list(counts.items())
items.sort(key= lambda x:x[1],reverse = True)
print("{2}\t{0:<10}\t{1:>5}".format("人名","出场次数",'序号'))
for i in range(20):
    word , count = items[i]
    print("{2}\t{0:<10}\t{1:>5}".format(word,count,'序号'))
