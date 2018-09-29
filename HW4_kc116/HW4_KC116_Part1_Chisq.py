# coding: utf-8

# In[2]:


from __future__ import print_function
__author__= 'kc116'

import pylab as pl
import numpy as np
import matplotlib as mp

import seaborn
from scipy.optimize import curve_fit, minimize
    
get_ipython().run_line_magic('pylab', 'inline')


# In[4]:


distributions = ['chisq']
mymean = 100
df = mymean


# In[9]:


md = {}

md['chisq'] = np.random.chisquare(df, size=100)

#print(md)
pl.hist(md['chisq'], bins = 30)
pl.ylabel('N')
pl.xlabel('x')


# In[10]:


print ("Chisq mean: %.2f, standard deviation: %.2f"%(md['chisq'].mean(), md['chisq'].std()))


# In[14]:


mysize = (2000 / (np.array(range(1, 100)))).astype(int)

print (mysize, mysize.shape)


# In[35]:


md['chisq'] = {}

for n in mysize:
    md['chisq'][n] = np.random.chisquare(df, size = n)


#print(md['chisq'])
md['chisq']['means'] = {}
axchisq_mu_n = pl.figure(figsize=(10,6)).add_subplot(111)

for nn in md['chisq']:
    if not type(nn) == str:
        md['chisq']['means'][nn] = md['chisq'][nn].mean()
        
        axchisq_mu_n.plot(nn, md['chisq']['means'][nn], 'o')
        axchisq_mu_n.set_xlabel('sample size', fontsize=18)
        axchisq_mu_n.set_ylabel('sample mean', fontsize=18)
        axchisq_mu_n.set_title('Chi squared', fontsize=18)
        axchisq_mu_n.plot([min(mysize), max(mysize)], [df, df], 'k')


# In[22]:


print('\033[1m' +'Figure 2: The Law of Large Numbers suggests that the majority of random numbers generated will fall close to the mean. In this case, as calculated above, the mean is around 100.28.')


# In[32]:


print('\033[0m')


# In[25]:


allmeans = list(md['chisq']['means'].values())

pl.figure(figsize=(10, 10))
pl.hist(allmeans,bins=30)
pl.xlabel('sample mean', fontsize = 18)
pl.ylabel('N', fontsize = 18)


# In[27]:


print('\033[1m' + 'Figure 3: This is a histogram of the mean of all samples')
print('\033[1m')

