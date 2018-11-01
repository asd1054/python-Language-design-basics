'''
官网自带的发邮件
特别麻烦

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 发送邮箱服务器
smtpserver = 'smtp.sina.com'
# 发送邮箱用户/密码
user = 'username@sina.com'
password = '123456'
# 发送邮箱
sender = 'username@sina.com'
# 接收邮箱
receiver = 'receive@126.com'
# 发送邮件主题
subject = 'Python email test'

# 编写HTML类型的邮件正文
msg = MIMEText('<html><h1>你好！</h1></html>','html','utf-8')
msg['Subject'] = Header(subject, 'utf-8')


# 连接发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()

所以有一个模块yagmail
两行代码实现发邮件

'''

import yagmail
user = '18586515730@163.com'
password = input("请输入密码：")
#host = 	'smtp.qq.com'
#port = '465'# 465 or 587
subject = input("请输入主题")
contents = input("请输入内容")

#yag = yagmail.SMTP(user=user,password=password,host = 'pop.qq.com',port = '995')

#链接邮箱服务器
yag = yagmail.SMTP( user=user, password=password, host='smtp.163.com',port='465')

yag.send ('269220442@qq.com',subject=subject,contents)