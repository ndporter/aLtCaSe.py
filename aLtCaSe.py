# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 13:04:30 2019

Python widget to convert any string to an obnoxious alternating case
Use at your own hazard

@author: ndporter@vt.edu

#usage example
t_str = 'This is a Test String'
aLtCaSe(t_str)
#returns 'tHiS Is a tEsT StRiNg'

"""

import math

def aLtCaSe(s):
    foo = ''
    for pos in range(len(s)):
        if math.remainder(pos,2)==0:
            foo = foo+str.lower(s[pos])
        else:
            foo = foo+str.upper(s[pos])
    return foo
