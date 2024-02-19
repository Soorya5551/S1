#!/usr/bin/env python
# coding: utf-8

# In[3]:


def getmax(lis):
    return max(lis,key=len)
n=int(input("Enter the number of words you want to enter:"))
lis=[]
for i in range(n):
    lis.append(input("Enter the word:"))
print("The longest word in the given list is:-",getmax(lis))    

    


# In[ ]:





# In[ ]:




