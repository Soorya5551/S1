#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Time:
	def __init__(self, hours, mins, sec):
		self.hours = hours
		self.mins = mins
		self.sec = sec
	def __add__(t1, t2):
		t3 = Time(0, 0, 0)
		if t1.mins + t2.mins > 60:
			t3.hours = (t1.mins + t2.mins) // 60
		t3.hours = t3.hours + t1.hours + t2.hours
		t3.mins = (t1.mins + t2.mins) % 60
		t3.sec = (t1.sec + t2.sec)
		return t3
	def displayTime(self):
		print("Time is ", self.hours, "hours ", self.mins, "minutes", "and", self.sec, "seconds")
	def displayMinute(self):
		print("Minutes:", self.hours * 60 + self.mins)
	def displaysecond(self):
		print("Second:", self.hours * 60 * 60 + self.mins * 60 + self.sec)

h1 = int(input("Enter time 1 in hour : "))
m1 = int(input("Enter time 1 in minutes :"))
s1 = int(input("Enter time 1 in second : "))
h2 = int(input("Enter time 2 in hour : "))
m2 = int(input("Enter time 2 in minutes : "))
s2 = int(input("Enter time 2 in second : "))

a = Time(h1, m1, s1)
b = Time(h2, m2, s2)
c = a + b
c.displayTime()
c.displayMinute()
c.displaysecond()


# In[ ]:




