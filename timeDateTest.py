import datetime


#d = '2016-10-21'

#t = "09:06:20.778644"

def stringToDatetime(d,t):
    dt = datetime.datetime.strptime('%s %s' %(d,t), '%Y-%m-%d %H:%M:%S.%f')
    return dt


