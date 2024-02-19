#!/usr/bin/env python
# coding: utf-8

# In[7]:


try: 
    fileptr = open("abc.txt","r")
    try: 
        fileptr.write("Hi I am Soorya")
    finally:
        fileptr.close()
        print("File closed")
except:
    print("Error")


# In[9]:


try: 
    fileptr = open("abc.txt","w")
    try: 
        fileptr.write("Hi I am Soorya")
    finally:
        fileptr.close()
        print("File closed")
except:
    print("Error")


# In[ ]:




