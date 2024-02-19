#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Bank:
	def _init_(self):
    		self.balance=0
    		print("__Create an Account__")
    		self.name=input("Enter the name :")
    		self.acctno=int(input("Enter the account number :"))
    		self.typeofac=input("Enter the type of account :")
	def deposit(self):
    		amount=int(input("Enter the amount to be deposited :"))
    		self.balance += amount
    		print("Amount Deposited :",amount)
	def withdraw(self):
    		amount=int(input("Enter the amount to be withdrawn :"))
    		if self.balance >= amount:
        		self.balance-=amount
    	   		print("Amount Withdrawn :", amount)
    		else:
        		print("Insufficient balance!")
	def display(self):
    		print("Account Balance :",self.balance)
a=Bank()
a._init_()
while(1):
	print("\n1.Deposit\n2.Withdrawal\n3.Balance\n4.Exit\n")
	ch=int(input("Enter your choice :"))
	if ch==1:
    		a.deposit()
	elif ch==2:
    		a.withdraw()
	elif ch==3:
    		a.display()
	else:
    		print("Wrong Choice!")
    		exit()


# In[ ]:




