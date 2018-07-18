
# coding: utf-8

# In[2]:


print ("hello world")


# In[5]:


a="hema"
print ("hai",a)


# In[6]:


a=int(input("enter a number"))
b=int(input("enter another number"))
c=a+b
print("Addition of two numbers:",c)


# In[23]:


import matplotlib.pyplot as plt
var=['a','b','c']
var1=[5.5,6.2,6.3]
plt.plot(var,var1)
plt.title("Height of students in a class")
plt.xlabel("Sections")
plt.ylabel("Height")
plt.show()
plt.savefig('fig.png')

