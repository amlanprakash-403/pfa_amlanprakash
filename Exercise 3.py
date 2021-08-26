#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Write a Python program to check whether the given number is even or not.

num = int(input('Enter the number you want to check for even or odd:   '))
if num%2 == 0:
    print('The number entered is even', num)
else:
    print('The number entered is odd', num)


# In[5]:


#Write a Python program to convert the temperature in degree centigrade to Fahrenheit. Use 30 C to F

T = float(input('Enter the temp  in degree celcius you want to convert into fahrenheit:  '))
F = ((T /100)*180  + 32)
print('The temp value you entered after converting into fahrenheit is:', F)


# In[7]:


#Python program to find the area of a triangle whose sides are given as 4, 3 and 6.
#S= (a+b+c)/2 Area = ssqrt(s*(s-a)*(s-b)*(s-c))

import math
a = 4
b = 3 
c = 6
S = (a+b+c)/2
Area = round(math.sqrt(S*(S-a)*(S-b)*(S-c)),2)
print('The area of the triangle is:', Area)


# In[8]:


#Python program to find the circumference and area of a circle with a given radius

import math
radius = float(input('Enter the value of radius : '))
area = round(math.pi * (radius **2),2)
circumference  = round(math.pi * (radius) * 2 ,2)
print('The area for the radius you entered is:', area)
print('The circumference for the radius you entered is:', circumference)


# In[10]:


#Python program to check whether the given integer is a multiple of 5

num = int(input('Enter the number you want to check to be a multiple of 5 or not: '))
if num% 5== 0:
    print('The number you entered is a multiple of 5')
else:
    print('The number you entered is not a multiple of 5')


# In[ ]:




