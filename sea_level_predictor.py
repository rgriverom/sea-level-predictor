import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    
    
    # Create scatter 
    scatter = df.plot.scatter(x="Year", y="CSIRO Adjusted Sea Level", c="red")
    slope, intercept, r_value, p_value, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    
    xmin = df["Year"].min()
    predict_year = np.arange(xmin, 2051,1) 
    # Create first line of best fit
    scatter.plot(predict_year, predict_year*slope + intercept)

    # Create second line of best fit
    year = df["Year"]>=2000
    slope, intercept, r_value, p_value, std_err = linregress(df[year]["Year"], df[year]["CSIRO Adjusted Sea Level"])
    predict_year = np.arange(2000, 2051,1)
    scatter.plot(predict_year, slope*predict_year+intercept, c="green")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea_level_plot.png")
    return plt.gca()