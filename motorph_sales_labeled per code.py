#!/usr/bin/env python
# coding: utf-8

# library import

# In[1]:


import pandas as pd

df = pd.read_csv("MotorPH_Sales Data-3rd Quarter-Year 2025.csv")

print(df.head(50))


# checking column names

# In[2]:


df.columns


# checking of rows and columns

# In[3]:


df.shape


# checking data types

# In[4]:


df.dtypes


# checking missing values

# In[5]:


df.isnull().sum()


# checking for duplicates

# In[6]:


df[df.duplicated()]


# checking for duplicated sales rows

# In[7]:


df[df.duplicated(keep=False)]


# dropping/cleaning duplicated sales rows

# In[8]:


df = df.drop_duplicates()


# verifying

# In[9]:


df.duplicated().sum()


# handling missing values

# In[10]:


df.isnull().sum()


# renaming columns

# In[11]:


df = df.rename(columns={
    "date": "Date",
    "client_type": "Client Type",
    "product": "Product",
    "unitprice": "Unit Price",
    "quantity": "Quantity",
    "total": "Total",
    "payment": "Payment Method"
})


# data report

# In[13]:


df.info()


# In[14]:


df.to_csv("MotorPH_Sales_Preprocessed.csv", index=False)


# In[15]:


# summary (e+0^n means scientific notation. kumbaga 1e+03 = 1*10^3 = 1000)
print("\nBASIC STATISTICAL SUMMARY")
print(df.describe())


# In[16]:


# mode of payment counter (included this kasi hindi siya nalabas sa basic statistical summary)
print("\nPAYMENT METHOD")
payment_counts = df["Payment Method"].value_counts(dropna=False)
payment_percentages = payment_counts / len(df) * 100

print(payment_counts)
print("\nPercentage:")
print(payment_percentages.round(2))


# In[17]:


#




