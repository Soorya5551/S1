#!/usr/bin/env python
# coding: utf-8

# In[1]:


num=int(input("Enter a number:"))
sum=0
temp=num
while temp>0:
    R=temp%10
    sum=sum+(R**3)
    temp//=10
if num==sum:
    print(num,"is an amstrong number.")
else:
    print(num,"is not an amstrong number.")


# In[2]:


num=int(input("Enter a number:"))
sum=0
temp=num
while temp>0:
    R=temp%10
    sum=sum+(R**3)
    temp//=10
if num==sum:
    print(num,"is an amstrong number.")
else:
    print(num,"is not an amstrong number.")


# In[ ]:




