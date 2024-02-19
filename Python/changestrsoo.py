#!/usr/bin/env python
# coding: utf-8

# In[6]:


def changechar(str):
    str=input("Enter a string:")
    a=list(str)
    first=a[0]
    char="$"
    for i in range(1,len(str)):
        if(a[i]==first):
            a[i]=char
    newstr=''.join(a) 
    return newstr
print("The changed string is:",changechar(str))           
       


# In[ ]:





# In[ ]:




