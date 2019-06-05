
# coding: utf-8

# In[79]:

import numpy as np
import pandas as pd
diseases_set=pd.read_csv('test1.csv')
diseases_set.shape


# In[80]:

diseases_set.head()


# In[81]:

diseases_set.iloc[2]


# In[82]:

dict={'Fever':0,'Cough':1,'Runny nose':2,'Headache':3,'Breathlessness':4,'Diarrhea':5,'Abdominal pain':6,'Vomiting':7,'Nosebleed':8,'Dizziness':9,'Insomnia':10,'Eye swelling':11,'Redness in eye':12,'Nausea':13,'Sweating':14,'Fatigue':15,'Joint pain':16} 

sim_list=[]

inp=['Fever','Runny nose','Cough','Fatigue'] ##### Input from the flask form part
for i in range(0,17):
    sim_list.append(0);

for i in range(len(inp)):
    key=dict.get(inp[i]);
    sim_list[key]=1;


def similarity_score(a,b):
    sim=0
    for i in range(len(a)):
        sim=sim+a[i]*b[i]
    return sim

    


# In[83]:

similar=0
temp=0
index=0;
a1=""
for i in range(0,20): 
    a=[]
    for j in diseases_set.iloc[i]:
        a.append(j)
    similar=similarity_score(a[1:],sim_list)
    if(similar>temp):
        a1=a[0]
        index=i
        temp=similar

    
print(a1)      
print(index)
print(temp)


# In[ ]:




# In[ ]:



