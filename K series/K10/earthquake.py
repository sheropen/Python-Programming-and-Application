#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
with open("all_month.csv",encoding ="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    depths,mags = [],[]
    for row in reader:
        try:
            depths.append(float(row['depth']))
        except:
            depths.append(0)
        try:
            mags.append(float(row['mag']))
        except:
            mags.append(0)
            
print(f"总次数：{len(mags)}")
print(f"最小震源深度：{min(depths):.2f}",f"最大震源深度：{max(depths):.2f}",
      f"平均震源深度：{sum(depths)/len(depths):.2f}")
print(f"最小震级：{min(mags):.2f}",f"最大震级：{max(mags):.2f}",
      f"平均震级：{sum(mags)/len(mags):.2f}")


# In[2]:


from matplotlib import cm
plt.figure(figsize = (15,10))
plt.grid()
plt.hist(depths,100,color='blue')
plt.xlabel('Depth(km)')
plt.ylabel('Frequency')
plt.title('FREQUENCY BY DEPTHS',fontdict = {'fontweight':'bold','fontsize':18})
plt.show()


# In[3]:


plt.figure(figsize = (15,5))
plt.grid()
plt.hist(mags,100,color='r')
plt.xlabel('Magnitute')
plt.ylabel('Frequency')
plt.title('FREQUENCY BY MAGNITUDES',fontdict = {'fontweight':'bold','fontsize':18})
plt.show()


# In[4]:


plt.figure(figsize = (15,5))
plt.grid()
plt.scatter(depths,mags,3,color='green')
plt.xlabel('Depth')
plt.ylabel('Magnitude')
plt.title('MAGNITUDES TO DEPTHS',fontdict = {'fontweight':'bold','fontsize':18})
plt.show()

