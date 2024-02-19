#!/usr/bin/env python
# coding: utf-8

# In[1]:


num=int(input("Enter the number:"))
a=0
b=1
if(num<=0):
    print("Enter a positive number!!")
elif num==1:
     print(num)
else:
    print(a)
    print(b)
    for i in range (1,num):
        c=a+b
        a=b
        b=c
        print(c)    


# In[ ]:




