#!/usr/bin/env python
# coding: utf-8

# In[2]:


a=[]
print("Square matrix")
n=int(input("Enter number of rows and columns: "))
b={}
a=[[]*n for i in range (n)]
print("\n Enter the elements of matrix: ")
for i in range(0,n):
    for j in range (0,n):
        a[i].append(int(input()))
print ("\nGiven matrix: \n",a)
for i in range (0,n):
    for j in range (0,n):
        if a[i][j]!=0:
              b[(i,j)]=a[i][j]
print("Dictionary is :",b)


# In[ ]:





# In[ ]:




