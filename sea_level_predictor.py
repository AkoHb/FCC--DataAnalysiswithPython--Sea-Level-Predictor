import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# constants
start_year = 1880
middle_year = 2000
end_year = 2050

# titles
image_tittle = 'Rise in Sea Level'

# data axis keys 
x_axis_data = 'Year'
y_axis_data = 'CSIRO Adjusted Sea Level'

# axis labels
x_axis_label = 'Year'
y_axis_label = 'Sea Level (inches)'

# image file name
image_name = 'sea_level_plot.png'

# line colors
line1_color = 'r'
line2_color = 'green'

def draw_plot():
    # Read data from file
    data = pd.read_csv("./epa-sea-level.csv")
    df = data.copy()
    x = df[x_axis_data]
    y = df[y_axis_data]
    
    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(x, y)

    # Create first line of best fit
    res = linregress(x, y)
    # print(res)
    x_pred = pd.Series([year for year in range(start_year, end_year + 1)])
    y_pred = res.slope * x_pred + res.intercept
    plt.plot(x_pred, y_pred, line1_color)

    # Create second line of best fit
    new_df = df.loc[df[x_axis_data] >= middle_year]
    new_x = new_df[x_axis_data]
    new_y = new_df[y_axis_data]
    res_line = linregress(new_x, new_y)
    # print(res)
    x_pred_line = pd.Series([year for year in range(middle_year, end_year + 1)])
    y_pred_line = res_line.slope * x_pred_line + res_line.intercept
    plt.plot(x_pred_line, y_pred_line, line2_color)


    # Add labels and title
    ax.set_xlabel(x_axis_label)
    ax.set_ylabel(y_axis_label)
    ax.set_title(image_tittle)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig(image_name)
    return plt.gca()