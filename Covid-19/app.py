from flask import Flask, jsonify, render_template, request
from functions import *
import pandas as pd 
import matplotlib.pyplot as plt
import csv
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.backends.backend_svg import FigureCanvasSVG
from matplotlib.figure import Figure


df = open_as_df("select * from state_history;", connect(param_dic))
# C:\Users\Tirhas\Desktop\GitHub\Project-2\Covid-19\Static\data
#import csv with 2020 covid data 
corona_df2 = pd.read_csv('..\..\Static\data\covid19.csv')
by_region =  corona_df2.groupby('Province_State').sum()[['Confirmed', 'Deaths', 'Recovered', 'Active']]
cdf = by_region.nlargest(2625, 'Confirmed')[['Confirmed']]

#create a function that will return updated data frame
def find_top_confirmed():
    corona_df2 = pd.read_csv('covid19.csv')
    by_region =  corona_df2.groupby('Province_State').sum()[['Confirmed', 'Deaths', 'Recovered', 'Active']]
    cdf = by_region.nlargest(2625, 'Confirmed')[['Confirmed']]
    return cdf

#import new csv with updated 2021 covid data 
corona_df = pd.read_csv('..\..\Static\time_series_covid_19_confirmed_US.csv') #4/3/2020

def find_top_confirmed2021():
    corona_df = pd.read_csv('time_series_covid_19_confirmed_US.csv')
    #only sum the data in the time series to remove the string columns 
    by_region= corona_df.iloc[:,11:].sum(axis=1)[['Confirmed', 'Deaths', 'Recovered', 'Active']]
    
    #group by states and summarize the total amount of cases
    total_list = corona_df.groupby('Province_State')['2/27/2021'].sum().tolist() #2/27/2020
    
    #add and set states in to a list
    state_list = corona_df["Province_State"].tolist()
    state_set = set(state_list)
    state_list = list(state_set)
    state_list.sort()

    #adding it to dataframe and only pulling the columns needed 
    new_df = pd.DataFrame(list(zip(state_list, total_list)), columns =['Province_State', 'Total_Cases'])
    return new_df

def all_covid():
    combined = pd.merge(cdf, new_df, left_on='Province_State', right_on='Province_State') #merge the two dataframes to compare 
    combined_clean = combined.rename(columns = {'Confirmed': 'Confirmed As of April 2020', 'Total_Cases': 'Confirmed As of Feb 2021'}, inplace = False) #rename the columns for clarity to show comparison/increase over period 
    sortedDf = combined_clean.sort_values("Confirmed As of Feb 2021", axis = 0 , ascending = False,inplace = False, na_position ='first') #sort to show the highest cases in the states 
    return sortedDf

def create_plot():
    Feb_2021 = sortedDf['Confirmed As of Feb 2021']
    April_2020 = sortedDf['Confirmed As of April 2020']
    states = sortedDf['Province_State'] #.nlargest(n=5, keep='first')


    x = np.arange(len(states))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, Feb_2021, width, label='Feb 2021', color="yellow")
    rects2 = ax.bar(x + width/2, April_2020, width, label='April 2020', color="green" )

    # Add some text for labels, title and custom x-axis tick labels, etc.
    dim = np.arange(1,25,1);
    ax.set_ylabel('Confirmed cases')
    #ax.set_ylim([0,4000])
    ax.set_xlim(1, 10)
    ax.set_title('Confirmed Cases April 2020 Vs Feb 2021 (Michigan Rank #14)')
    ax.set_xticks(dim)
    ax.set_yscale('log')
    ax.set_xticklabels(states, rotation=90)
    ax.legend()

app = Flask(__name__)

# Route to render plot.html template using data from Mongo
@app.route('/')
def plot():

    bar = create_plot()
    return render_template('plot.html', plot=bar)
    


    

if __name__ == "__main__":
    app.run(debug=True)
