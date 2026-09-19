#!/usr/bin/env python
# coding: utf-8

# library import

# In[40]:


import pandas as pd

df = pd.read_csv("MotorPH_Products_List_2025.csv")

print(df.head(50))


# checking column names

# In[41]:


df.columns


# checking of rows and columns

# In[8]:


df.shape


# checking data types

# In[10]:


df.dtypes


# checking missing values

# In[21]:


df.isnull().sum()


# checking for duplicates

# In[13]:


df[df.duplicated()]


# checking for duplicated product names

# In[15]:


df[df["EntrName"].duplicated(keep=False)]


# dropping/cleaning duplicated product names

# In[22]:


df = df.drop_duplicates()


# verifying

# In[17]:


df.duplicated().sum()


# handling missing values

# In[19]:


df.isnull().sum()


# renaming columns

# In[38]:


df = df.rename(columns={
    "EntrName": "Product Name",
    "EntrNo": "Product ID Number",
    "EntrDetails": "Product Types",
    "Manufacturing Date": "Date of Manufacturing",
    "Acquisiton": "Date of Acquisition",
    "UnitPrice": "Unit Price"
})


# reorder

# In[39]:


df = df[
    [
        "Product ID Number",
        "Product Name",
        "Product Types",
        "Unit Price",
        "Date of Manufacturing",
        "Date of Acquisition"
    ]
]


# data report

# In[43]:


df.info()


# In[45]:


df.to_csv("MotorPH_Products_Preprocessed.csv", index=False)


# In[ ]:




