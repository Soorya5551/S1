#!/usr/bin/env python
# coding: utf-8

# In[2]:


def add():
    a=int(input("Enter the 1st no:"))
    b=int(input("Enter the 2nd no:"))
    c=a+b
    print("Sum is",c)
add()


# In[3]:


def add(a,b):
    c=a+b
    print("Sum is",c)
add(3,5)


# In[4]:


def add(a,b=5):
    c=a+b
    print("Sum is",c)
add(3)


# In[5]:


def add(a,b=5):
    c=a+b
    print("Sum is",c)
add(3,6)


# In[6]:


def add(a,b):
    c=a+b
    return c
x=int(input("Enter the 1st number"))
y=int(input("Enter the 2nd number"))
z=add(x,y)
print("Sum is:",z)


# In[ ]:




