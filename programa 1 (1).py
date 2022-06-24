# -*- coding: utf-8 -*-
"""
Created on Thu May 26 11:09:50 2022

@author: SL5
"""

letters = []

# Let's push some letters into our list
letters.append('c')
letters.append('a')
letters.append('t')
letters.append('g')

# Now let's pop letters, we should get 'g'
last_item = letters.pop()
print(last_item)

# If we pop again we'll get 't'
last_item = letters.pop()
print(last_item)

# 'c' and 'a' remain
print(letters) # ['c', 'a']