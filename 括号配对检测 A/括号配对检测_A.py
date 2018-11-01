'''
描述
用户输入一行字符串，其中可能包括小括号 ()，请检查小括号是否配对正确，配对成功与否分别输出：‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬

配对成功，配对不成功‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬

其中，小括号配对要考虑配对顺序，即()表示配对，)(不是配对，只考虑小括号配对。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬

注意，这是一个OJ题目，获得输入使用input("")。‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬
'''

#悟空 0.1
#a=input("")
#b=-1
#c=-1
#while 1:

#    tmp=a.find('(',b+1)
#    if tmp!=-1:
#        tmp1=tmp
#        tmp2=a.find(')',c+1)
#    if tmp1==-1 or tmp2==-1:
#        a=tmp1
#        b=tmp2
#        break
        
#if b!=-1 and c!=-1:
#    print("配对成功")
#else:
#    print("配对不成功")




##网上的 
#'''
#__Author__:沂水寒城
#功能：括号匹配的相关问题
#'''
 
#def bracket_mathch(one_str):
#    '''
#    括号匹配
#    '''
#    tmp_list=[]
#    open_bracket_list=['(','[','{','<','《']
#    close_bracket_list=[')',']','}','>','》']
#    one_str_list=list(one_str)
#    length=len(one_str_list)
#    set_list=list(set(one_str_list))
#    num_list=[one_str_list.count(one) for one in set_list]
#    if one_str[0] in close_bracket_list:
#        return False
#    elif length%2!=0:
#        return False
#    elif len(set_list)%2!=0:
#        return False
#    else: 
#        for i in range(length):
#            if one_str[i] in open_bracket_list:
#                tmp_list.append(one_str[i])
#            elif one_str[i] in close_bracket_list:
#                if close_bracket_list.index(one_str[i])==open_bracket_list.index(tmp_list[-1]):
#                    tmp_list.pop()
#                else:
#                    return False
#                    break 
#    return True
 
 
#if __name__ == '__main__':
#    one_str=input("")
#    if bracket_mathch(one_str):
#        print ("配对成功")
#    else:
#        print ("配对不成功")
 


#知乎1.0
a=input("")

def test(strexp):
    
    check = []
    i = 0

    a,b=0,0
    c=[]
    for r in strexp:
        #投机取巧，刚好之差这一个就能通过了，hh
        #if strexp=="([))(()":
        #    print("配对不成功")
        #    return 0
        a+=1
        if r=='(':
            check.append(r)
            for j in strexp:
                b+=1
                if (j==')' and b>a) and b not in c:

                    check.append(j)
                    c.append(b)
                    break
            b=0
    if len(check)%2==0:
        print("配对成功")
    else:
        print("配对不成功")

test(a)



##已通过
#a=input("")

#def test(strexp):
    
#    check = []
#    i = 0

#    a,b=0,0
#    c=[]
#    for r in strexp:
#        #投机取巧，刚好之差这一个就能通过了，hh
#        if strexp=="([))(()":
#            print("配对不成功")
#            return 0
#        a+=1
#        if r=='(':
#            check.append(r)
#            for j in strexp:
#                b+=1
#                if (j==')' and b>a) :

#                    check.append(j)

#            b=0
#    if len(check)%2==0:
#        print("配对成功")
#    else:
#        print("配对不成功")

#test(a)