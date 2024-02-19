#!/usr/bin/env python
# coding: utf-8

# In[5]:


str1=input("Enter the 1st string:")
str2=input("Enter the 2nd string:")
def change(str1,str2):
    first=str1[0]
    second=str2[0]
    a=list(str1)
    b=list(str2)
    a[0]=second
    b[0]=first
    newstr1=''.join(a)
    newstr2=''.join(b)
    final=newstr1+' '+newstr2
    return final
print("Joined word with swapping letters in first position is:",change(str1,str2))


# In[ ]:




