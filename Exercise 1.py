#!/usr/bin/env python
# coding: utf-8

# In[1]:


#In the below exercise, one solved example is given and one unsolved. You are required to code the the unsolved example

print(5/8)


# In[2]:


#In question 1 ,above the print(7 + 10), add the comment # Addition

#Addition

print(7 + 10)


# In[3]:


#Practice some more mathematical operations and display the output. Comment(#?) what each print command is doing

#Addition and Subtrction

print(5+5)
print(5-5)

#Multiplication , Subtraction , Division and Raise to the Power 

print(3*5)
print(10/2)
print(18%7)
print(4**2)


# In[6]:


#Solve the following questions of Simple Interest using Python

#John invests $5,000 in a savings account at an annual interest rate of 7% for 5 years. (a) How much money did he earned in interest?

p = float(5000)
r = float(0.07)
t = float(5)
SI = p*r*t
print(SI)



#(b) What is the total value of his savings account at this point

Total = p + SI
print(Total)


# In[14]:


#Sally invests $8,000 into an account paying an annual interest rate of 8.7%. How many years will it take for her to earn $4,872 in interest?

p = float(8000)
r = float(0.087)
SI = 4872
#SI = p*r*t
t = SI/(p * r)
print(t)


# In[16]:


#Marie invests $3,000 into a savings account. In 4 years , she earns a total of $768 in interest. What is the annual interest rate offered by this account?

p = float(3000)
t = float(4)
SI = 768
#SI = p*r*t
r = SI/(p * t)*100
print(r)


# In[17]:


#Suppose you have $100, which you can invest with a 10% return each year. Add code to calculate amount you end up with after 7 years, and print the result.

print(100 + (100*10*7/100))


# In[ ]:




