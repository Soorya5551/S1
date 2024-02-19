#!/usr/bin/env python
# coding: utf-8

# In[1]:


num1=int(input("Enter the 1st number:"))
num2=int(input("Enter the 2nd number:"))
op=input("Enter operator +,-,*,%,^")
if(op=="+"):
    print("Sum is:",(num1+num2))
elif(op=="-"):
    print("Difference is:",(num1-num2))
elif(op=="*"):
    print("Product is:",(num1*num2))
elif(op=="%"):
    print("Remainder is:",(num1%num2))
elif(op=="^"):
    print("Power is:",(num1**num2))
else:
    print("No operator entered")


# In[ ]:




