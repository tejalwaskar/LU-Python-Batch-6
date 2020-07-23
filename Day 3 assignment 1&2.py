#!/usr/bin/env python
# coding: utf-8

# # Assignment 1

# 1) sum of n numbers with the help of while loop

# In[1]:


sum1=0
while True:
    num1=int(input("Enter the value"))
    sum1=sum1+num1
    print(sum1)
    if num1==0:
        break
print("Sum of number is", sum1)


# # Assignment 2

# 2) take a integer and find it is prime o not

# In[2]:


num=int(input("Enter a number:"))
for i in range(2,num):
    if num%i==0:
        print("Not prime")
        break
else:
    print("Prime")


# In[ ]:





# In[ ]:




