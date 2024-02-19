#!/usr/bin/env python
# coding: utf-8

# In[10]:


num=int(input("Enter the number of students:"))
studlist=[]
for i in range(0,num):
    stud={}
    stud['Name']=input("Enter the name:")   
    stud['Roll No:']=int(input("Enter the Roll No:"))
    studlist.append(stud)
print(studlist)    
print("Name and Roll No:")
for i in range(num):
    print(studlist[i])


# In[ ]:




