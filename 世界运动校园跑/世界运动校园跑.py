
'''
学期目标：130公里
2018.09.25-2018.12.30
5+31+30+30
总：96天
每日上限：3公里
每次最低要求：2公里
配速：2'12''~10'00''分钟/公里
即上限：2'12''
下限：10'00''
'''
import math 
goal=130
#journey_max=3
#journey_min=2
speed_max=2*60+12#速度最大
speed_min=10*60#速度最小
for i in [2,3]:
    
    day = 130/i
    print("如果每天跑{}公里，就至少需要跑{}天".format(i,day))
    speed = i/speed_max
    #speed = math.fmod(speed,60)
    print("如果一天跑一公里{}，则")

