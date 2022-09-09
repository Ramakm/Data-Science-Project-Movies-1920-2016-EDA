#!/usr/bin/env python
# coding: utf-8

# In[1]:


# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session


# In[2]:


movies = pd.read_csv("/kaggle/input/movies/Movies.csv")
movies


# In[3]:


# Highest Grossing amount 

Gross_amount = movies["gross"].sort_values(ascending=False)
Gross_amount.head(10)


# In[4]:


#Converting a column of the dataframe to a list

genres_list = movies["genres"].head(10).to_list()
language_list = movies["language"].unique()
movies["budget"] = movies["budget"].astype(int)
budget_value = movies["budget"].head(5).to_list()


# In[5]:


genres_list


# In[6]:


language_list


# In[7]:


# Find out the index of IMDB rating 

movies.columns.to_list().index("imdb_score")

# First i converted all the columns to a list then applied the index() method. As dataframe doesn't have any index() method


# In[8]:


# This will print the values of movies whose rating are common and sort them in descending ordeer

# The most is 6.7. Nearly 175 movies are rated 6.7

import matplotlib.pyplot as plt

plt.title("Most Common Movie Ratings on IMDB", size = 15, color = "blue")
plt.xlabel("IMDB_Ratings", color = "blue")
plt.ylabel("No Of Movies", color = "blue")

movies["imdb_score"].value_counts().sort_values(ascending = False).head().plot(kind="bar", color = "orange")


# ### Finding out which country has produced the most gross amount from movies till 2016.

# In[9]:


# Used pivot table for this solution

gross_amount_by_each_country = pd.pivot_table(data = movies, values = 'gross', index = 'country',aggfunc = sum).sort_values(by='gross', ascending= False).head(10)
gross_amount_by_each_country


# In[10]:


gross_amount_by_each_country_imdb = pd.pivot_table(data = movies, values = 'movie_title', index = 'country',columns = 'imdb_score',aggfunc = sum)

gross_amount_by_each_country_imdb.sort_index(ascending = False).head()


# In[11]:


best_country_produced = movies[(movies["country"]== "USA") | (movies["country"]== "UK") | (movies["country"]== "Germany") | (movies["country"]== "India") ]


# In[12]:


best_country_produced.head()


# In[13]:


pd.pivot_table(best_country_produced,
index ="country",
values = ["gross","budget"],
aggfunc={"gross":np.sum,"budget":np.sum}).plot(kind='bar', figsize = (8,5))
plt.title ("Gross vs Budget", color = "red", size = 15)


# In[14]:


movies.set_index("actor_1_name", inplace = True)


# In[15]:


movies


# In[16]:



movies.loc[["Johnny Depp"]].plot(kind = "scatter", x = "movie_title",y ="num_critic_for_reviews",figsize= (10,7))
plt.title("Johnny Depp Movies vs Critics Score", color = "red", size = 10)
plt.xticks(rotation=90)
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 10
      }
plt.rc('font', **font)


# In[17]:


movies.reset_index().head()


# In[18]:


Best_movies_in_USA = movies[(movies.imdb_score >8) & (movies.budget >230000000)]


# In[19]:


Best_movies_in_USA.reset_index()


# In[20]:


Best_movies_in_IND = movies[(movies.imdb_score >7) & (movies.budget >2300000) & (movies.country == 'India')]


# In[21]:


Best_movies_in_IND.reset_index()


# ## Let's Work on The Filtered Movie Data

# In[22]:


import pandas as pd
import numpy as np


# In[23]:


pip install openpyxl


# In[24]:


movies_df = pd.read_excel("../input/movies-filtered-data/Movies_filtered_data.xlsx")
movies_df


# ### Visualizing all the details of each lead actors in tree map way.

# In[25]:


import plotly.offline as py
import plotly.express as px
fig = px.treemap(movies_df, path=['lead_role','movie_title'],
                  color='movie_title', hover_data=['imdb_score','budget', 'num_voted_users'],color_continuous_scale='green')
autosize=True
py.iplot(fig)

#Just Double Click on any of teh box and hover over a box, You will see the full details.
#After double clicks That box will expand and it will be easy to visible and read the details.


# **Fill the null value with 0**

# In[26]:


movies_df= movies_df.fillna(0)
movies_df.head()


# **Count the No of Movies produced only in USA**

# In[27]:


total_USA_movies =  movies[movies["country"] == "USA"]
total_USA_movies.shape


# **Grouping Each Country and summing all the columns values respectively**

# In[28]:


country_sum = movies.groupby("country").sum()
country_sum.head()


# In[ ]:




