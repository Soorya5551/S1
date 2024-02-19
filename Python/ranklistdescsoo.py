#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=int(input("Enter the number of students:"))
studlist=[]
for i in range(0,n):
    stud={}
    stud["name"]=input("Enter the name:")
    stud["roll"]=int(input("Enter the roll number:"))
    stud["mark"]=int(input("Enter the mark:"))
    studlist.append(stud)
for i in range(1,n):
    for j in range(0,n-1):
        if(studlist[j]["mark"]<studlist[j+1]["mark"]):
            temp=studlist[j]
            studlist[j]=studlist[j+1]
            studlist[j+1]=temp
           
for i in range(0,n):
        print(studlist[i])


# In[ ]:




