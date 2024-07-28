#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


# In[21]:


#uploding data set we use pd.read_csv() function
data = pd.read_csv("apple_products.csv")
print(data.head())


# In[22]:


# for checking null valuse we used isnull().sum() function

print(data.isnull().sum())


# In[23]:


# to check descirptive statistics of data we used describe() function

print(data.describe())


# I phone sales analysis in India
# 
# Now i wil create a new dataframe by storing all the data about top 10 highest rated iphones.in India on flipcart. It will help in understanding what kind of iphone are liked the most in india.

# In[27]:


highest_rated = data.sort_values(by=["Star Rating"],ascending=False)
highest_rated=highest_rated.head(10)
print(highest_rated['Product Name'])


# Now let's have a llok at the number of ratings of the higest iPhone on flipcart

# In[28]:


iphones = highest_rated["Product Name"].value_counts()
label = iphones.index
counts = highest_rated["Number Of Ratings"]
figure = px.bar(highest_rated, x=label,y=counts,
               title="Number of Ratings of Highest Rated iPhones")
figure.show()


# according to above graph apple iphone 8 Plus(Gold,64 GB) has the most ratings on flipkart.Now let's have a look at the number of reviews of the highest-rated iPhones on flipkart

# In[38]:


iphones = highest_rated["Product Name"]
lable = iphone.index
counts = highest_rated["Number Of Reviews"]
figure = px.bar(highest_rated, x=label,y=counts,
               title="Number of Reviews of Highest Rated iPhones")
figure.show()


# In[40]:


figure = px.scatter(data_frame = data, x="Number Of Ratings",
                   y="Sale Price",size="Discount Percentage",
                   trendline="ols",
                   title="Relationship between Sale Price and Number of Ratings")
figure.show()


# In[42]:


figure = px.scatter(data_frame = data, x="Number Of Ratings",
                   y="Discount Percentage",size="Sale Price",
                   trendline="ols",
                   title="Relationship between discount percentage and Number")
figure.show()


# In[ ]:




