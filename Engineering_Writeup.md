# Real-Time Data Pipeline & Dashboard for US Earthquake Analytics  

By Nicholas Bronson

## Abstract:

This project seeks to create a partially automated data pipeline to examine data on earthquakes. The final product pulls data from the [USGS’s earthquake database](https://earthquake.usgs.gov/) in real time and easily stores and sends this data to a [Streamlit dashboard](https://share.streamlit.io/bronsonnh/streamlit_repo/main/nick-app.py) in which a user can examine qualities and trends in earthquakes across the US over time. Recent newsflow suggests that there may have been an increase in earthquakes in Oregon and off its coast in 2021. This project attempts to answer the question: has there in fact been an uptick in the number of significant earthquakes occurring in the Oregon region recently? 

## Design:

This project's focus is on using a sizable amount of USGS's data to create an interactive tool to examine earthquakes in Oregon specifically, while also empowering and encouraching users to explore other earthquakes. In achieving this goal, data must be pulled, processed, stored, and finally connected to the Streamlit app. The goall is to do this in a manner in which manual processes are reduced to a minimum, and process are as logical, maintainable, and efficent as possible. Please see the Algorithms section below for additional details.  

## Data:

The originally pulled data consists of 869141 rows of data and 22 features including time of earthquake, id, longitude and latitude, depth, magnitude, and among others. The data is collected and updated in real-time, with a brief process with a minimal number of manual steps. There is an increasing amount of data which is housed in a local SQL database, and routinely uploaded to GitHub and Streamlit thereafter. 

## Algorithms:

To begin the process of creating a data pipeline that was deployed into the dashboard, a CSV containing historical data from the USGS earthquake API was pulled. The acquired data was information on all earthquakes from 2010 to the present date that were recorded within the US. This data was uploaded into a SQLite database, and pulled into a Jupyter notebook using pySpark. PySpark was also used to clean the data prior to converting the pySpark dataframe to Pandas dataframe in which further cleaning and manipulation was carried out. A process that allows all new US earthquake data to be pulled from USGS’s database was created, and this can be executed by selecting a new file name and a single click. A preprocessing framework was developed that allows new data to be cleaned and reformatted to a more easily usable format by means of running a single cell in a Jupyter notebook. 

Data was uploaded to GitHub and deployed to a live Streamlit app. This Streamlit app contains general information regarding earthquakes to provide basic information to a user of this app who may not have knowledge of earthquakes. Additionally, this app contains interactive maps that allow a user to see where earthquakes occurred during each month between 2010 and the present date. This data can also be filtered by magnitude. The project concludes that while more research may need to be done, the uptick in earthquakes in Oregon appears to be massive, although, newsflow suggests this hasn't caused damage or loss of life. 

## Tools:

Tools used for this project include SQLite for storing data, PySpark for manipulating and cleaning the data, Python, and libraries including Matplotlib and Seaborn visualizing for writing code that populates the web app which runs through Streamlit Share. GitHub was used to host data used by Streamlit to visualize and allow users to interact with data. 

## Communications:

The primary forms of communication for this project are a PowerPoint presentation and a Streamlit web app. The Streamlit web app is freely available at [this link](https://share.streamlit.io/bronsonnh/streamlit_repo/main/nick-app.py) and can be used to examine information regarding the number of earthquakes and magnitude of earthquakes occurring since 2010 in the United States. 





