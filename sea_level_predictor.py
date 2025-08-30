import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    df = pd.read_csv("epa-sea-level.csv")

    fig, ax = plt.subplots(figsize=(10,8))
    ax.scatter(y='CSIRO Adjusted Sea Level', x='Year', data=df)


    regressao = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = np.arange(1880, 2051)
    y = [((i * regressao[0]) + regressao[1]) for i in x]

    regressao2 = linregress(df[df['Year'] >= 2000]['Year'], df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level'])
    x2 = np.arange(2000, 2051)
    y2 = [((i * regressao2[0]) + regressao2[1]) for i in x2]

    ax.plot(x,y)
    ax.plot(x2,y2)

    ax.set_xlabel('Year')
    ax.set_title('Rise in Sea Level')
    ax.set_ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()