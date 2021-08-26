#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Create a variable savings with the value 100. Check out this variable by typing print(savings) in the script.

savings = 100
print(savings)


# In[6]:


#Create a variable growth_multiplier, equal to 1.1. Create a variable, result, equal to the amount of money you saved after 7 years. Print out the value of result

growth_multiplier = 1.1
time_years = 5
money = round(float(savings * growth_multiplier * time_years),2)
print('The money you recieve after 7 years is:', money)


# In[10]:


#Create a new string, desc, with the value "compound interest" Create a new boolean, profitable, with the value True.

amount = round(savings*(1.1**7),2)
desc = amount - savings

print('The amount of Compound Interest you recieve after 7 years is :', desc)

# Create a variable :Profitable
Profitable = True
# Now checking the types of the variables
print(type(savings))
print(type(desc))
print(type(growth_multiplier))
print(type(Profitable))


# In[12]:


#Assign a value to these variables as shown
#A= 10.7
#B = “This is python course”
#C = False
#Check the type of variables A, B, C
#Also Check the type of variables savings, profitable, desc,growth_multiplier

A = 10.7
B = 'This is python course'
C = False
print(type(A))
print(type(B))
print(type(C))

# Calculate the product of savings and growth_multiplier and state the results in year1
year1 = round(savings * growth_multiplier,2)
print('The value of the variable year1 is:', year1)


# In[14]:


#Calculate the product of savings and growth_multiplier. Store the result in year1. What do you think the resulting type will be? Find out by printing out the type of year1. Calculate the sum of desc and desc and store the result in a new variable doubledesc. Print out doubledesc. Did you expect this?

year1 = round(savings * growth_multiplier,2)
print('The value of the variable year1 is:', year1)
print(type(year1))

## Assign the sum of desc and desc to doubledesc
doubledesc = desc + desc
print(doubledesc)


# In[25]:


#Assuming the integer savings and float result are defined as savings = 100 result = 100 * 1.10 ** 7
# Print the following line print("I started with $" + savings + " and now have $" + result + ". Awesome!")
# Fix the error by changing type of variables

#Definition of savings and result

savings = 100
result = 100 * 1.10**7

#Fix the printout using str()
print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")


# In[33]:


#Convert the variable pi_string to a float and store this float as a new variable, pi_float . Multiply pi_float by 2 and save it in double_pi

# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float
pi_float = float(pi_string)

double_pi = pi_float *2
print('The value of double_pi is', double_pi)


# In[36]:


#Which one of these will throw an error?

print("I can add integers, like " + str(5) + " to strings.")
print("I said " + str("Hey " * 2) + "Hey!")
print("The correct answer to this multiple choice exercise is answer number " + 2)
print(True + False)


# In[ ]:




