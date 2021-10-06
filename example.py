#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=1


# In[2]:


print(a)


# In[3]:


a=1
b=2
print(a+b)


# In[4]:


a='amar'
b='nath'
print(a+b)


# In[ ]:





# In[6]:


a = 1.001
print(a)


# In[7]:


a = 1.234434
b = 23.333
c = a + b
print(c)


# In[8]:


def add(a, b):
    c = a + b
    return c
x = 10
y = 20
z = add(x, y)
print(z)
    


# In[14]:


def add(a, b):
    c = a+b;
    return c
x = 10
y = 20
z = add(x, y)
print(z)


# In[16]:


# This function adds two number,
# input arguments - integers,
# output - integer
# logic - addition
def add(a, b):
#     adding two numbers
    c = a+b
#     returning the value
    return c

# This function multiplies two number,
# input arguments - integers,
# output - integer
# logic - addition
def mul(a, b):
    c = a*b
    return c

# z is a global variable
z = add(10, 20)
z = mul(z, 10)
print(z)


# In[30]:


# 1 1 2 3 5 8
# 1 2 3 4 5 6
# fibonacci series
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    return (fib(n-1) + fib(n-2))

p = 50
f = fib(p)
print(f)

# Dynamic Programming
        


# In[ ]:


# Input: grid n*n

# output: number of paths


n = 2
n = 3
n = 100
n = 500

n = 100000


# In[ ]:


1 1 2

1 1 2 3 5


# In[31]:


# Tower of honoii

Problem:
number of disks is 3


# In[ ]:


n = 4

n = 5
 n = 20 // You cannot solve this problem -> Open challenging problem


# In[ ]:


# Any given problem:
#     Understand the problem
# Plot the graph -> Power of 3 // Factorial (limit the number if the number of records 10000) 
# // Quadratic / Linear


# In[38]:


# Lists // Array

a = [10, 20, 30]

b = [40, 50, 60]

print(a)
print(b)

c = a + b
print(c)
# Reverse function
print(c[::-1])


# In[41]:



a = [10, 10.5, 201.0001, '12323']


# In[42]:


a


# In[43]:


c = a+b


# In[44]:


c


# In[48]:


a[3]


# In[50]:


l = len(a)


# In[54]:


print(a)
for v in a:
    print(v)


# In[57]:


print(a)
for i in range(len(a)):
    print(a[i])


# In[67]:


a = [10, 20, 30, 40, 101, 200, 2222, 2232, 123]
for i in range(1, len(a), 3):
    print(a[i])


# In[69]:


i = 0
while i < len(a):
    print(a[i])
    i=i+1


# In[70]:


# Tuple

# Hashmap
# Key and Value

a = {}
print(a)


# In[71]:


a[1] = 'Amar'


# In[72]:


a


# In[73]:


a[2] = 'sat'


# In[74]:


print(a)


# In[75]:


print(a[2])


# In[ ]:


# Questions, I know the value, can you me the key?


# In[76]:


print(b)


# In[77]:


a[3] = b


# In[78]:


print(a)


# In[79]:


c = {}


# In[ ]:


Dynamic memory allocation
int a = (int *) malloc(n*size(int))
a reference // Integer


# In[80]:


d = {}


# In[81]:


d[1] = 'Rat'


# In[82]:


d


# In[83]:


a[4] = d


# In[84]:


print(a)


# In[ ]:


# JSON processing 
# XML


# In[85]:


d  = {}


# In[86]:


e = [99, 200, 33]


# In[87]:


d[2] = e


# In[88]:


a


# In[89]:


a[4] = d


# In[90]:


print(a)


# In[91]:


print(a[4])


# In[92]:


print(a[4][2])


# In[93]:


print(a[4][2][1])


# In[ ]:




