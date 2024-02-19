#!/usr/bin/env python
# coding: utf-8

# In[2]:


n=int(input("Enter the limit:"))
def sum(n):
    if(n<=1):
        return n
    else:
        return n+Sum(n-1)
print("The sum is:",sum(n))


# In[ ]:





# In[ ]:





# In[ ]:




