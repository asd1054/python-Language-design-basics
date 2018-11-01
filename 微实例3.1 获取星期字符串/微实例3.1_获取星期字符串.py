weekstr = "星期一星期二星期三星期四星期五星期六星期日"
weekid = eval(input("请输入星期数字（1-7）："))
pos = (weekid - 1)*3
print(weekstr[pos:pos+3])
