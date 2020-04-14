# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 10:47:30 2020

@author: Harshini
"""

import re
s=input("Enter a string:")
if(re.search('[a-k][0369][a-z A-Z 0-9 #]',s)):
    print("True")
else:
    print("False")