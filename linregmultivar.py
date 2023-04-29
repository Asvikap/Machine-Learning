#!/usr/bin/env python
# coding: utf-8

# <h2 style="color:green" align="center"> Machine Learning With Python: Linear Regression Multiple Variables</h2>

# <h3 style="color:purple">Sample problem of predicting home price in monroe, new jersey (USA)</h3>

# Below is the table containing home prices in monroe twp, NJ. Here price depends on **area (square feet), bed rooms and age of the home (in years)**. Given these prices we have to predict prices of new homes based on area, bed rooms and age.

# <img src="homeprices.jpg" style='height:200px;width:350px'>

# Given these home prices find out price of a home that has,
# 
# **3000 sqr ft area, 3 bedrooms, 40 year old**
# 
# **2500 sqr ft area, 4 bedrooms,  5 year old**

# We will use regression with multiple variables here. Price can be calculated using following equation,

# <img src="equation.jpg" >

# Here area, bedrooms, age are called independant variables or **features** whereas price is a dependant variable

# In[1]:


import pandas as pd
import numpy as np
from sklearn import linear_model


# In[2]:


df = pd.read_csv('C:\\Harsha\\VIT\\Fall20192020\\AI\\u4\\LiReg Multi\\homeprices.csv')
df


# **Data Preprocessing: Fill NA values with median value of a column**

# In[3]:


df.bedrooms.median()


# In[5]:


df.bedrooms = df.bedrooms.fillna(df.bedrooms.median())
df


# In[6]:


reg = linear_model.LinearRegression()
reg.fit(df.drop('price',axis='columns'),df.price)


# In[7]:


reg.coef_


# In[8]:


reg.intercept_


# **Find price of home with 3000 sqr ft area, 3 bedrooms, 40 year old**

# In[9]:


reg.predict([[3000, 3, 40]])


# In[10]:


112.06244194*3000 + 23388.88007794*3 + -3231.71790863*40 + 221323.00186540384


# **Find price of home with 2500 sqr ft area, 4 bedrooms,  5 year old**

# In[11]:


reg.predict([[2500, 4, 5]])


# <h3>Exercise<h3>

# In exercise folder (same level as this notebook on github) there is **hiring.csv**. This file contains hiring statics for a firm such as experience of candidate, his written test score and personal interview score. Based on these 3 factors, HR will decide the salary. Given this data, you need to build a machine learning model for HR department that can help them decide salaries for future candidates. Using this predict salaries for following candidates,
# 
# 
# **2 yr experience, 9 test score, 6 interview score**
# 
# **12 yr experience, 10 test score, 10 interview score**
# 

# <h3>Answer<h3>

# 53713.86 and 93747.79
