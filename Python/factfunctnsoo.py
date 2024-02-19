#!/usr/bin/env python
# coding: utf-8

# In[1]:


def recur_fact(num):
    if num==1:
        return num
    else: 
        return num*recur_fact(num-1)
num=int(input("Enter the number:"))   
if num<0:
        print("Sorry factorial does not exist for negative number.")
elif num==0:
        print("The factorial of 0 is 1.")
print("The factorial of",num,"is",recur_fact(num))


# In[ ]:




