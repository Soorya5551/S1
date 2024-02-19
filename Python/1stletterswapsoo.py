#!/usr/bin/env python
# coding: utf-8

# In[8]:


def swap(str):
    str=input("Enter a string:")
    new=list(str)
    first=new[0]
    last=new[-1]
    newstr=last+str[1:-1]+first
    return newstr
print("The new string after swapping is:",swap(str))


# In[ ]:





# In[ ]:




