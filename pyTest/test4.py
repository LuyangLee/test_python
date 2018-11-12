#!/usr/bin/env python3
#-*- coding:utf-8 -*-

monthDay = [0,31,59,90,120,151,181,212,243,273,304,334,365]

def isleapYear(year):
    if (year % 400 == 0) or ((year % 100 != 0) and (year % 4 ==0)):
        return True
    else:
        return False

date = input("输入年月日如20180816\n")
year = int(date[0:4])
month = int(date[4:6])
day = int(date[6:8])
dayth = 0

    
