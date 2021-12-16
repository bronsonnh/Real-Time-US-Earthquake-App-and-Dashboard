import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn  as sns
from PIL import Image

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
    data = pd.read_csv('/Users/nicholasbronson/Metis_Nick/eq_df_2.csv')
    return data

data = upload_data()

n_eqs = len(data[data["year"] == 2021])


"""
## Basic Earthquake Facts:
Number of Earthquakes in the US in 2021:

"""
st.header(n_eqs)


n_eqs_two_point_five_or_more = len(data[data["year"] == 2021])

"""
Number of Earthquakes in the US in 2021 over 2.5 Magnitude:
"""



"""
To provide a bit of context, please see the table below provided by 
"""

image = Image.open('/Users/nicholasbronson/Metis_Nick/eapp/eq_table.png')
st.image(image)


"""
# Map With Sliders to filter by month, year, earthquakes greater than a given strength.
"""

##Filter Creation - Filters for Month, Year, and Magnitude
month_input = st.slider('Month Filter', int(data['month'].min()), int(data['month'].max()))
year_input = st.slider('Year Filter', int(data['year'].min()), int(data['year'].max()))
mag_input = st.slider('Magnitude Filter', int(data['mag'].min()), int(data['mag'].max()))

month_filter = data['month'] == month_input
year_filter = data['year'] == year_input
mag_filter = data['mag'] >= mag_input

st.map(data.loc[month_filter & year_filter & mag_filter, ['latitude', 'longitude']])



"""
## Number of Earthquakes by Year
"""
year_groups = data.groupby([data['year']])['year'].count()
year_value_counts = data['year'].value_counts(sort=False, ascending = False)
year_value_counts = year_value_counts.reindex(index=year_value_counts.index[::-1])
year_value_dict = dict(year_value_counts) 

fig, axs = plt.subplots(1, 2, figsize=(9, 3))
axs[0].bar(year_value_dict.keys(), year_value_dict.values())
axs[1].hist(year_value_dict.values())
fig.suptitle('Categorical Plotting')
st.pyplot(fig)


"""
Looking specifically at Oregon.
"""

or_boundary = data[data['latitude'].between(42,46.5) & data['longitude'].between(-130,-116.4)]

month_input_o = st.slider('Month Filter Oregon', int(or_boundary['month'].min()), int(or_boundary['month'].max()))
year_input_o = st.slider('Year Filter Oregon', int(or_boundary['year'].min()), int(or_boundary['year'].max()))
mag_input_o = st.slider('Magnitude Filter Oregon', int(or_boundary['mag'].min()), int(or_boundary['mag'].max()))

month_filter_o = or_boundary['month'] == month_input_o
year_filter_o = or_boundary['year'] == year_input_o
mag_filter_o = or_boundary['mag'] >= mag_input_o

st.map(or_boundary.loc[month_filter_o & year_filter_o & mag_filter_o, ['latitude', 'longitude']])





