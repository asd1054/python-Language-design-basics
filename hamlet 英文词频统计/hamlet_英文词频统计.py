
#英文分词 统计

excludes = {"the","and","of","you",'i','a','i','is','my','in','to','it','his','with','your','for','be','he'}
def getText():
    txt = open("hamlet.txt",'r').read()
    txt = txt.lower()
    for ch in '!"#$%()*+,-.,/:;<=>?@[]\\^_`{|}~':
        txt.replace(ch,' ')
    return txt

hamletText = getText()
words = hamletText.split()
counts = {}
for word in words :
    counts[word] = counts.get(word,0)+1
    if word in excludes:
        del counts[word]
items = list(counts.items())
items.sort(key = lambda x:x[1],reverse = True)
print("序号\t{0:15}{1:<5}".format('单词','出现次数'))
for i in range (100):
    word ,count = items[i]
    print("{2:3}\t{0:15}{1:>8}".format(word,count,i+1))