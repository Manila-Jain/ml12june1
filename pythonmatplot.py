
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[15]:


x=[2,6]
y=[4,9]
x1=[8,3]
y1=[4,7]
plt.xlabel("time")
plt.ylabel("speed")
plt.plot(x,y,label="ml learning")
plt.plot(x1,y1,label="big data learning")
#plt.show()
plt.legend()
plt.grid(color="b")
plt.show()


# In[27]:


x=[200,60,34,90]
#y=[200,60,34,90]
y=["v","r","s","y"]
plt.xlabel("time")
plt.ylabel("speed")
plt.bar(y,x,label="river",color="y")
plt.legend()
plt.grid(color="g")
plt.show()


# In[29]:


x=[2,6,5,6,7,78,8]
y=[4,9,23,6,9,6,5]
x1=[2,9,5,6,2,38,8]
y1=[5,8,24,5,8,2,5]
plt.xlabel("time")
plt.ylabel("speed")
plt.scatter(x,y,label="river",marker='x', s=120,c='r')
plt.scatter(x1,y1,label="mountain",marker='o', s=150)
plt.legend()
plt.show()

