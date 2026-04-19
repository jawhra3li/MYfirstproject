#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install numpy


# In[3]:


import numpy as np
print(np.__version__)


# In[6]:


arr=np.array([1,2,3,4]
           )


# In[7]:


arr


# In[10]:


arr=np.array([[1,2,2,2],[1,4,6,8]]
)


# In[11]:


arr


# In[13]:


list1=[1,3,4,5]
myarray=np.array(list1)


# In[14]:


list1


# In[15]:


list2d=[[1,3,4,5],[2,2,3,3]]
myarray=np.array(list2d)


# In[16]:


myarray


# In[17]:


myarray.shape


# In[21]:


colnum=myarray.shape[1]


# In[22]:


colnum


# In[23]:


myarray.dtype


# In[25]:


arryz0=np.zeros(3,'int')
print(arryz0)


# In[26]:


arryz1=np.ones(3,'float')
print(arryz1)


# In[31]:


arrayones=np.ones([3,10],'int')
print(arrayones)


# In[32]:


digarry=np.eye(5)
print(digarry)


# In[34]:


rangarry=np.arange(0,50,2)
print(rangarry)


# In[35]:


mult=arryz0*arryz1
print(mult)


# In[36]:


rangarry*3


# In[37]:


rangarry**3


# In[38]:


rangarry-2


# In[39]:


rangarry.T


# In[40]:


rangarry.shape


# In[42]:


rangarry[2]


# In[43]:


rangarry[1:3]


# In[47]:


rangarry[:6]


# In[48]:


myarray[0:2,:]


# In[49]:


myarray


# In[50]:


myarray[0:1,2:3]


# In[51]:


myarray[0:2,1:3]


# In[52]:


D=np.array([1,2,3,4])


# In[54]:


D[0:1]=100
print(D)


# In[55]:


D[0:3]=100
print(D)


# In[56]:


myarray[1,2]=100
print(myarray)


# In[57]:


myarray[1:3,:]=100
print(myarray)


# In[58]:


myarray[1]


# In[59]:


myarray[0]


# In[61]:


nwearr=np.arange(1,13)
nwearr


# In[63]:


reshapp=nwearr.reshape((3,4))
reshapp


# In[64]:


reshapp=nwearr.reshape((2,5))
reshapp


# In[65]:


reshapp=nwearr.reshape((2,6))
reshapp


# In[68]:


x=np.array([1,2,2])
y=np.array([1,3,2])
result=np.concatenate([x,y])
result


# In[70]:


eresult=result.reshape(2,3)
eresult


# In[72]:


s=([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
v=([[ 1,  2,  5,  4],
       [ 2,  6,  7,  8],
       [ 9, 10, 18, 12]])
result2=np.concatenate([s,v])
result2


# In[73]:


result2=np.concatenate([s,v],axis=0)
result2


# In[74]:


result2=np.concatenate([s,v],axis=1)
result2


# In[80]:


result3=([[ 1,  2,  3,  4,  1,  2,  5,  4],
       [ 5,  6,  7,  8,  2,  6,  7,  8],
       [ 9, 10, 11, 12,  9, 10, 18, 12]])
upper,lower=np.vsplit(result3,[2])
print(upper)


# In[87]:


grid=np.arange(1,17).reshape((4,4))
upper,lower=np.vsplit(grid,[2])
print(upper)
print("__________")
ua,l=np.hsplit(grid,[2])
print(ua)


# In[88]:


grid=np.arange(20).reshape((4,5))
upper,lower=np.vsplit(grid,[2])
print(upper)
print("__________")
ua,l=np.hsplit(grid,[2])
print(ua)


# In[90]:


grid=np.arange(20).reshape((4,5))
upper,lower,new=np.vsplit(grid,[2,3])
print(upper)
print("__________")
print(lower)
print("___________")
print(new)


# In[94]:


arrr=([[0, 1, 2, 3, 4],
 [5 ,6 ,7, 8 ,9]])
aa=np.sqrt(arrr)
bb=np.exp(arrr)
print(aa)
print("_______")
print(bb)


# In[97]:


x=np.random.randint(2,100,20)
x


# In[98]:


arrr=([[0, 1, 2, 3, 4],
 [5 ,6 ,7, 8 ,9]])
aa=np.sqrt(arrr)
bb=np.exp(arrr)
np.add(aa,bb)


# In[99]:


x=np.array([1,2,2])
arrr=([[0, 1, 2, 3, 4],
 [5 ,6 ,7, 8 ,9]])
aa=np.sqrt(arrr)
np.add(aa,x)


# In[101]:


x=np.array([1,2,2])
y=np.array([100,200,300])
condition=np.array([True,True,False])
ans=np.where(condition,x,y)
ans


# In[102]:


x=np.array([1,2,2])
y=np.array([300])
condition=np.array([True,True,False])
ans=np.where(condition,x,y)
ans


# In[104]:


x=np.array([2,2,0])
y=np.array([300])
condition=np.array([False,True,False])
ans=np.where(condition,x,y)
ans


# In[107]:


arr=np.random.randn(5,5)
arr


# In[108]:


np.where(arr<0,0,arr)


# In[109]:


np.where(arr<0,False,arr)


# In[110]:


np.where(arr>0,True,arr)


# In[111]:


arr.sum()


# In[113]:


arr.sum(0)


# In[114]:


arr.sum(1)


# In[115]:


arr.mean()


# In[116]:


arr.std()


# In[117]:


arr.var()


# In[118]:


boolary=np.array([True,False,True,False])
boolary.any()


# In[119]:


boolary=np.array([True,False,True,False])
boolary.all()


# In[120]:


array1=([  1,   2, 300])
np.sort(array1)


# In[121]:


array1=([  1,   2, 300])
-np.sort(array1)


# In[ ]:




