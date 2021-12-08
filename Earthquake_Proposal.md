# Proposal: Earthquake Dashboard to Display Trends   

# Question/Need:

Recent newsflow suggests increased earthquake activity off the shore of Oregon. While reading articles on earthquakes can give you a level of insight into the situation, it would be helpful to provide a resource in which earthquake activity can be easily analyzed, and compared to past periods. The question is as follows:

Can a resource be deployed that will process earthquake data and allow an individual to look at and better understand earthquake trends and how they develop over time?

This project will aim to give a user of this resource the ability to compare time periods, number of earthquakes, magnitude, and severity trends. 

# Data Description:
I will use historical and real-time data from [USGS](https://www.usgs.gov/programs/earthquake-hazards/earthquakes)regarding earthquake date, location, depth, magnitude, and several other features. I plan to use at least 10 years of historical data, starting with earthquakes in the US, however, I may expand the scope of the project to include earthquakes in other locations or perhaps globally. This model will be automated to pull real-time data on a daily basis. 

# Tools: MongoDB will be used to store the data. I plan to use Flask or Streamlit to deploy an application that can be used to easily select two different dates or time periods and compare several figures regarding earthquakes between those two dates. I also intend to use Spark to handle the data. Python may be used for exploratory analysis. 

# MVP Goal: 
The MVP goal will be a dashboard in which you can compare earthquake trends between different periods. This will include an option to find average earthquake strength, visualize earthquakes through graphs showing trends over time. 
