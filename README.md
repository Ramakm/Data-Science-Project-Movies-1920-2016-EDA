# DataScience-Project-Movie_Data_Visualization-1920-2016
This project is all about the movies ever produced in all languages from 1920 to 2016. Covered most of the movies.

## Attaching the visualtions Used in this projects 
```
plt.title("Most Common Movie Ratings on IMDB", size = 15, color = "blue")
plt.xlabel("IMDB_Ratings", color = "blue")
plt.ylabel("No Of Movies", color = "blue")

movies["imdb_score"].value_counts().sort_values(ascending = False).head().plot(kind="bar", color = "orange")
```
![IMBD vs Critics](https://user-images.githubusercontent.com/8182816/189283758-186bf1b9-3d33-4a1b-87e9-c30395f88189.png)

```
movies.loc[["Johnny Depp"]].plot(kind = "scatter", x = "movie_title",y ="num_critic_for_reviews",figsize= (10,7))
plt.title("Johnny Depp Movies vs Critics Score", color = "red", size = 10)
plt.xticks(rotation=90)
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 10
      }
plt.rc('font', **font)

```
![Jhonny Depp vs Critics](https://user-images.githubusercontent.com/8182816/189283871-81770598-990e-4baf-8ddd-21d7a85c9603.png)

```
pd.pivot_table(best_country_produced,
index ="country",
values = ["gross","budget"],
aggfunc={"gross":np.sum,"budget":np.sum}).plot(kind='bar', figsize = (8,5))
plt.title ("Gross vs Budget", color = "red", size = 15)
```
![Gross vs Budget](https://user-images.githubusercontent.com/8182816/189283935-f3999c7d-35c4-425a-b60c-2396e2530415.png)


```
import plotly.offline as py
import plotly.express as px
fig = px.treemap(movies_df, path=['lead_role','movie_title'],
                  color='movie_title', hover_data=['imdb_score','budget', 'num_voted_users'],color_continuous_scale='green')
autosize=True
py.iplot(fig)
```
![Robert De Jenero Movies](https://user-images.githubusercontent.com/8182816/189283960-fca8ea6b-65ce-4982-8499-fb3709169437.png)

