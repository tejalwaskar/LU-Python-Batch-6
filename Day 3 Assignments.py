#!/usr/bin/env python
# coding: utf-8

# # Assignment 1

# 1) sum of n numbers using while loop

# In[3]:


sum1=0
while True:
    num1=int(input("Enter the value"))
    sum1=sum1+num1
    print(sum1)
    if num1==0:
        break
print("Sum of number is", sum1)


# # Assignment 2

# 2) Take a number and find out it is prime or not

# In[2]:


num=int(input("Enter a numbr"))
for i in range(2,num):
    if num%i==0:
        print("Not prime")
        break
else:
    print("Prime")


# In[ ]:




