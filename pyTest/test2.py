#!/usr/bin/env python3
#-*- coding:utf-8 -*-
from collections import Iterable

l = input()
ladder = [0, 10, 20, 40, 60, 100]
rate = [0, 0.1, 0.075, 0.05, 0.03, 0.015, 0.01]

def compute(l):
    ladder.reverse()
    rate.reverse()
    sum = 0
    for index,profits in enumerate(ladder):
        if l < profits:
            continue
        a = l -profits
        sum += a * rate[index]
        l = profits
    return sum
        
print(compute(int(l)))

