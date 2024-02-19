#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cmath
a=int(input("Enter a value for a:"))
b=int(input("Enter a value for b:"))
c=int(input("Enter a value for c:"))
d=(b**2)-(4*a*c)
sol1=(-b+cmath.sqrt(d))/(2*a)
sol2=(-b-cmath.sqrt(d))/(2*a)
print("The solution of the quadratic equation are{}:".format(sol1,sol2))


# In[ ]:





# In[ ]:




