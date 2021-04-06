from flask import Flask, jsonify, render_template
from functions import *
import pandas as pd 
import folium

df = open_as_df("select * from state_history;", connect(param_dic))


corona_df = pd.read_csv('covid19.csv')
by_region =  corona_df.groupby('Province_State').sum()[['Confirmed', 'Deaths', 'Recovered', 'Active']]
cdf = by_region.nlargest(2625, 'Confirmed')[['Confirmed']]


def find_top_confirmed(n = 15):
    corona_df = pd.read_csv('covid19.csv')
    by_region =  corona_df.groupby('Province_State').sum()[['Confirmed', 'Deaths', 'Recovered', 'Active']]
    cdf = by_region.nlargest(2625, 'Confirmed')[['Confirmed']]
    return cdf


corona_df = pd.read_csv('covid19.csv')
corona_df=corona_df.dropna()
m=folium.Map(location=[34.223334,-82.461707],
            tiles='Stamen toner',
            zoom_start=8)
def circle_maker(x):
    folium.Circle(location=[x[0],x[1]],
                 radius=float(x[2])*10,
                 color="red",
                 popup='{}\n confirmed cases:{}'.format(x[3],x[2])).add_to(m)
corona_df[['Lat','Long_','Confirmed','Combined_Key']].apply(lambda x:circle_maker(x),axis=1)
html_map=m._repr_html_()


# Create an instance of Flask
app = Flask(__name__)

# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    return render_template("home.html",table=cdf, cmap=html_map)

if __name__ == "__main__":
    app.run(debug=True)
