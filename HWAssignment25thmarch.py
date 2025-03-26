# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 16:49:30 2025

@author: dell
"""

#1.Write a Python program to create a tuple.

# t1=(1,2,'Hello',)
# print("tuple is",t1 )

#2.Write a Python program to create a tuple with different data types

# t2=(1,2,3,'Hello',[4,5,6])
# print(t2)

#3.Write a Python program to create a tuple with numbers and print one item.

# t3=(10,20,30,40,50)
# print(t3[3])

#4.Write a Python program to unpack a tuple in several variables.

# t4=(10,20,30)
# x,y,z=t4
# print(x)
# print(y)
# print(z)

#5. Write a Python program to add an item in a tuple.

# t5=(1,3,5,7,9)
# new=t5+(4,)
# print("new tuple is ",new)

#6. Write a Python program to convert a tuple to a string.

# t= ('H', 'e', 'l', 'l', 'o')
# result = ""
# for char in t:
#     result += char


# print("Converted string:", result)

# 7.Write a Python program to get the 4th element and 4th element from last of a tupel

# t6=(10,20,30,40,50,60,70,80,90)
# forth_element=t6[3]
# print("4th element is ",forth_element)
# forth_last=t6[-4]
# print("4th last element is ",forth_last)

#8.write a Python program to reverse a tuple.

# t6=(10,20,30,40,50,60,70,80,90)
# reverse=t6[::-1]
# print("reverse of tupel is", reverse)

#9.Write a Python program to find the repeated items of a tuple


# t6=(10,20,30,40,50,60,70,80,90,10,50)
# t7=[]
# repeted=[]
# for i in t6:
#     if i in t7:
#         repeted.append(i)
#     else:
#         t7.append(i)
        
# print(repeted)        

#10.Write a Python program to check whether an element exists within a tuple.

# t=(10,20,30,40,50,60,70,80,90)

# n=int(input("Enter number :-"))
# if n in t:
#     print("number is in tuple ")
# else:
#   print("not in tuple") 


#11.Write a Python program to convert a list to a tuple.
# t=(10,20,30,40,50,60,70,80,90)

# l1=list(t)
# print(l1)

#12.Write a Python program to remove an item from a tuple.

# t=(10,20,30,40,50,60,70,80,90)
# n=int(input("Enter no. to remove:"))
# l1=list(t)
# l1.remove(n)

# t1=tuple(l1)

# print(t1)

#13. Write a Python program to slice a tuple.

# t=(10,20,30,40,50,60,70,80,90)

# t1=t[2:5]
# print(t1)

#14. Write a Python program to find the index of an item of a tuple.
# t=(10,20,30,40,50,60,70,80,90)
# n=int(input("Enter the number:"))

# print('index',t.index(n))


#15. Write a Python program to find the length of a tuple.
# t=(10,20,30,40,50,60,70,80,90)
# print(len(t))
 
#Write a Python program to sort list of tuple based on sum
# Input: [(4, 5), (2, 3), (6, 7), (2, 8)]
# Output: [(2, 3), (4, 5), (2, 8), (6, 7)]"

# t= [(4, 5), (2, 3), (6, 7), (2, 8)]

# result=sorted(t,key=sum)
# print(result)
    























 















