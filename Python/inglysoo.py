#!/usr/bin/env python
# coding: utf-8

# In[8]:


def stringadd(str1):
    length=len(str1)
    if length>2:
        if str1[-3:]=='ing':
            str1+='ly'
        else:
            str1+='ing'
    return str1 
print(stringadd('Watch'))
print(stringadd('Lov'))
print(stringadd('Smoothing'))


# In[ ]:




