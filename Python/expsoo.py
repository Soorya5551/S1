#!/usr/bin/env python
# coding: utf-8

# In[4]:


x=int(input("Enter the value of x:"))
n=int(input("Enter the value of n:"))
s=1
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return(f)
for i in range(1,n):
    s=s+(x**i)/fact(i)
print("The value of the exponential series is:",s)


# In[ ]:




