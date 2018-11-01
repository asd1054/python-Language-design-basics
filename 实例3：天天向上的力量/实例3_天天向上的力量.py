
#每一天努力1%，一年下来收益多少
dayup,dayfactor=1.0,0.01

    
daydown=pow(1-dayfactor,365)
    
dayup=pow(1+dayfactor,365)
print("一年365天，天天向上的力量：%.2f"%dayup)
print("一年365天，天天向下的力量：%.2f"%daydown)

#5天向上，2天向下
dayup,dayfactor=1.0,0.01
for i in range(365):
    if i % 7 in [6,0]:#周末休息的时候
        dayup=dayup*(1-dayfactor)
    else:
        dayup=dayup*(1+dayfactor)
print("一年365天，一个星期5天向上 2天向下的力量：%.2f"%dayup)

#求天天向上为多少，才能和别人天天向上的一样

dayfactor=0.01

#并不准确
def dayUp(dayfactor):
    dayup=1.0
    for i in range(365):
        if i % 7 in [6,0]:#周末休息的时候
            dayup=dayup*(1-0.01)
        else:
            dayup=dayup*(1+dayfactor)

    return dayup
while(dayUp(dayfactor)<=37.78):
    dayfactor+=0.0001
print("天天向上为{:.10f}，才能和别人天天向上的一样".format(dayfactor))