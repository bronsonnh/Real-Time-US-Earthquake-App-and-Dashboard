import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn  as sns
from PIL import Image
import numpy as np


st.set_option('deprecation.showPyplotGlobalUse', False)
sns.set_style('darkgrid')



"""
# Dashboard for Examining Earthquake Trends in the Conterminous US 
By Nicholas Bronson
\n
Welcome to this Earthquake dashboard. All data used in this model was aquired from the
United States Geological Survey's earthquake database linked [here](https://www.usgs.gov/programs/earthquake-hazards/earthquakes).
\n
This dashboard provides insight on frequency, location, and magnitude of earthquakes
in the conterminous United States.
\n
The genesis of my idea to create this dashboard came from [this NPR article.](npr.org/2021/12/08/1062365995/50-earthquakes-hit-off-the-oregon-coast-but-scientists-say-theyre-no-great-shake)
This dashboard will allow users to look into the earthquake data, and filter it in several different manners.
Perhaps you can answer the question: Have earthquakes been increasing in number or severity in the US, particularly on the West Coast.
"""


def upload_data():
    #Function to load csv data into streamlit  
    data = pd.read_csv('/Users/nicholasbronson/Metis_Nick/earthquake_updated_mr.csv')
    return data

data = upload_data()

n_eqs = len(data[data["year"] == 2021])
av_mag = round((data["mag"].mean()),2)
n_eqs_two_point_five_or_more = len(data[data["year"] == 2021])
avg_error = round((data["magError"].mean()),2)


"""
## Basic Earthquake Facts & Graphs:

###### Note the data considered is only for earthquakes with a magnitude of 2 or greater. 

### Number of Earthquakes in the US in 2021:

"""

st.header(n_eqs)


"""
### Average magnitude of earthquakes over the last 10 years:

"""
st.header(str(av_mag))


"""
### Average error in magnitude of reported earthquakes:
"""
st.header(avg_error)

st.write("The number above is the estimated standard error for the magnitude of all earthquakes examined.") 








"""
To provide a bit of context, please see the table below provided by 
"""

image = Image.open('/Users/nicholasbronson/Metis_Nick/eapp/eq_table_mr.png')
st.image(image)


"""
To understand the distribution of earthquake strength, please see the following histogram:

"""


fig = plt.figure(figsize=(10,4))
plt.hist(data["mag"], bins=30)
plt.xlabel("Earthquake Magnitude", fontsize=20)
plt.ylabel("Number of Earthquakes", fontsize=20)
plt.title("Distribution of Earthquake Strength", fontsize=20)
st.pyplot(fig)


"""
The graph below shows the number of earthquakes per year in the US, as you can see 2019-2021 it appears the number of earthquakes has increased.
While this graph does clearly demonstrate this, it is worth considering that perhaps measurement has become more precise, or more locations
that track earthquakes have come online.
"""
year_groups = data.groupby([data['year']])['year'].count()
year_value_counts = data['year'].value_counts(sort=False, ascending = False)
year_value_counts = year_value_counts.reindex(index=year_value_counts.index[::-1])
year_value_dict = dict(year_value_counts) 

fig = plt.figure(figsize=(10,4))
plt.bar(year_value_dict.keys(), year_value_dict.values())
plt.xlabel("Number of Earthquakes", fontsize=20)
plt.ylabel("Year", fontsize=20)
plt.title("Earthquakes per Year", fontsize=20)
st.pyplot(fig)



"""
# Map to display number of earthquakes, sliders to choose month, year, and strength of earthquakes displayed.
"""

##Filter Creation - Filters for Month, Year, and Magnitude
month_input = st.slider('Month Filter', int(data['month'].min()), int(data['month'].max()))
year_input = st.slider('Year Filter', int(data['year'].min()), int(data['year'].max()))
mag_input = st.slider('Magnitude Filter (strengths greater than or equal to selected input)', int(data['mag'].min()), int(data['mag'].max()))

month_filter = data['month'] == month_input
year_filter = data['year'] == year_input
mag_filter = data['mag'] >= mag_input

st.map(data.loc[month_filter & year_filter & mag_filter, ['latitude', 'longitude']])





"""
# Map with filters, specifically for Oregon
"""

or_boundary = data[data['latitude'].between(42,46.5) & data['longitude'].between(-130,-116.4)]

month_input_o = st.slider('Month Filter Oregon', int(or_boundary['month'].min()), int(or_boundary['month'].max()))
year_input_o = st.slider('Year Filter Oregon', int(or_boundary['year'].min()), int(or_boundary['year'].max()))
mag_input_o = st.slider('Magnitude Filter Oregon (strengths greater than or equal to selected input)', int(or_boundary['mag'].min()), int(or_boundary['mag'].max()))

month_filter_o = or_boundary['month'] == month_input_o
year_filter_o = or_boundary['year'] == year_input_o
mag_filter_o = or_boundary['mag'] >= mag_input_o

st.map(or_boundary.loc[month_filter_o & year_filter_o & mag_filter_o, ['latitude', 'longitude']])


"""
Looking at this map, the number of earthquakes in Oregon seem rather modest this year, over the last couple months. I have graphed the number of earthquakes per year below as well. 
"""

or_year_value_counts = or_boundary['year'].value_counts(sort=False, ascending = False)
or_year_value_counts = or_year_value_counts.reindex(index=year_value_counts.index[::-1])
or_year_value_dict = dict(or_year_value_counts) 

fig2 = plt.figure(figsize=(10,4))
plt.plot(or_year_value_dict.keys(), or_year_value_dict.values())
plt.xlabel("Year", fontsize=20)
plt.ylabel("Number of Earthquakes", fontsize=20)
plt.title("Number of Earthquakes per Year in Oregon", fontsize=20)
st.pyplot(fig2)

"""
# Conclusions and Next Steps
"""

"""
My conclusion is that there **does not** appear to be a significant uptick in earthquakes in 2021. While there has been a modest increase since 2020, it looks like 2011-2014 had a significantly higher number of earthquakes.
While I have come to this conclusion, there is certainly more work to be done. Please feel free to use the data below, or check out the [USGS website](https://www.usgs.gov/programs/earthquake-hazards/earthquakes) which has extensive information on earthquakes globally.
"""



"""
## Full dataframe for US earthquakes from 2010-2021 
"""
data

"## Full dataframe for Oregon earthquakes from 2010-2021"

or_boundary 

""" Thank you for visiting my streamlit app! I seek to update this page with additional features, please feel free to reach out at [bronsonnh@gmail](bronsonnh@gmail) or
we can chat on [LinkedIn](https://www.linkedin.com/in/nicholas-h-bronson-2b2b9774/) if you have any suggestions or thoughts on this app, or trends in earthquake prevalance."""

