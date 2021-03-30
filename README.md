# Project-2
-----------------------------------------
# Extraction

Data was extracted from a CSV file and possibly web scraping.

# Transformation

1. CSV file will be read into data frame and transformed. OR can be read by D3.csv method and used.
2. Data in some columns have to be parsed, counted and stored in additional columns.
3. Irrelevant columns need to be dropped.  Renaming and rearrangement of columns have to be done along with changing of data types to maintain uniformity and to present meaningful data.
  
# Loading
Data frame will be loaded into the relational database – Postgres or MongoDB.

# Flask Application 
Flask application will be utilized and data from the Postgres or Mongo DB database will derived to create endpoints that will contain json objects of necessary data from which maps and charts can be built.
Flask will also render the HTML template created to display all the features on the client web browser.
# HTML pages
2 or more HTML pages will be created that will have access the JavaScript file in order to display the dashboard features on the browser. 
# JavaScript file 
D3.js, Plotly and Leaflet libraries will provide the basic framework for building the Covid-19 information map and the different types of charts/plots. 
Research will be done to add a plugin or a new JS library to enhance the features of the display elements. 
