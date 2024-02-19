#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cmath
a=int(input("Enter a value for a:"))
b=int(input("Enter a value for b:"))
c=int(input("Enter a value for c:"))
s=(a+b+c)/2
A=(s*(s-a)*(s-b)*(s-c))**0.5
print("The area is:",A)


# In[2]:


import cmath
a=int(input("Enter a value for a:"))
b=int(input("Enter a value for b:"))
c=int(input("Enter a value for c:"))
s=(a+b+c)/2
A=cmath.sqrt((s*(s-a)*(s-b)*(s-c)))
print("The area is:",A)


# In[ ]:




