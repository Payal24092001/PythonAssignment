# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 13:30:36 2025

@author: dell
"""

#1. Write a Python program to combine two dictionary adding values for
#common keys. Go to the editor
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}

# for key in d1:
#     if key in d2:
#        d2[key]=d1[key]+d2[key]
#     else:
#         d2[key]=d1[key]
# print(d2)        

# 2.Write a Python program to print all unique values in a dictionary.

# d = [{'V': 'S001'}, {'V': 'S002'}, {'VI': 'S001'}, {'VI': 'S005'}, 
#         {'VII': 'S005'}, {'V': 'S009'}, {'VIII': 'S007'}]


# unique_values = {value for dic in d for value in dic.values()}


# print(unique_values)



#3Write a Python program to create a dictionary from a string.
#Track the count of the letters from the string. 'w3resource'

# x='w3resource'
# d={}

# for letter in x:
#     d[letter]=d.get(letter,0)+1
# print(d)
    
        

#4. Get the key corresponding to the minimum value from the following
# dictionary
# sampleDict = { 'Physics': 82, 'Math': 65, 'history': 75}


# new=sorted(sampleDict)
# print(new)

# print(new[0])

 
#5.Combine two dictionary adding values for common keys
# Input: dict1 = {'a': 12, 'for': 25, 'c': 9}
# dict2 = {'python': 100, 'java': 200, 'for': 300}
# Output: {'for': 325, 'python': 100, 'java': 200}

# d1={'a': 12, 'for': 25, 'c': 9}
# d2={'python': 100, 'java': 200, 'for': 300}

# for key in d1:
#     if key in d2:
#         d2[key]=d1[key]+d2[key]
    
# print(d2)    


# dict1={101:{“Apple” :10, “Mango” :5 },102 :{“Apple” :15, “Mango” :8, “Cherry” :5 },103: {“Apple” :10} }
# Output
# Dict2= {“ Apple” :35, “Mango” :13, “Cherry” :5 }

dict1 = {
    101: {"Apple": 10, "Mango": 5},
    102: {"Apple": 15, "Mango": 8, "Cherry": 5},
    103: {"Apple": 10}
}

dict2 = {}

for sub_dict in dict1.values():
    for fruit, quantity in sub_dict.items():
        dict2[fruit] = dict2.get(fruit, 0) + quantity

print(dict2)