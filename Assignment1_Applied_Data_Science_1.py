# -*- coding: utf-8 -*-
# Student ID - 22010606
# Student Name - Deepak Raj Palaniammal Kaliannan

import pandas as pd
import matplotlib.pyplot as plt
unemployment_rate = pd.read_excel(
    r"C:/Users/user/Downloads/unemployment_rate2.xlsx")
# print(unemployment_rate)
unemploymentdata = unemployment_rate.dropna()
print(unemploymentdata)
plt.figure()


def unemployment(x):
    """    
    This is a User defined function unemployment(x) has a pandas DataFrame x as input and 
    will plots the unemployment rates of different European countries from the year column of the DataFrame from their corresponding unemployment rates.	

    Parameters
    ----------
    x : Pandas DataFrame
        This is a DataFrame have columns for years and the unemploymnet rate of all countries in the file

    Returns
    -------
    None.
    The function only plots the unemployment rates of different European countries against the year, 
    and does not return any value.
    """
    # plotting line plot
    plt.figure(figsize=(20, 10))
    plt.plot(x['Year'], x['United kingdom'], label='United kingdom')
    plt.plot(x['Year'], x['Belgium'], label='Belgium')
    plt.plot(x['Year'], x['Netherlands'], label='Netherlands')
    plt.plot(x['Year'], x['Poland'], label='Poland')
    plt.plot(x['Year'], x['Germany'], label='Germany')
    plt.plot(x['Year'], x['Spain'], label='Spain')
    plt.plot(x['Year'], x['Portugal'], label='portugal')
    plt.plot(x['Year'], x['France'], label='France')
    plt.plot(x['Year'], x['Finland'], label='Finland')
    plt.plot(x['Year'], x['Italy'], label='Italy')
    plt.title(
        "UNEMPLOYMENT RATE  10 EUROPIAN COUNTRIES FROM 2012 TO 2021 ", fontweight="bold")
    # labelling
    plt.xlabel("Year", fontweight="bold")
    plt.ylabel("Unemployment Rate", fontweight="bold")
    plt.legend()
    # save figure
    plt.savefig("Unemployment_lineplot.png")
    plt.show()


# calling the function unemployment
unemployment(unemploymentdata)

best_shows = pd.read_csv(r"C:/Users/user/Downloads/best_shows_netflix.csv")
print(best_shows)


def barplot_for_voteseachgenre(x, y, z):
    """
    This is a User Defined function barplot_for_voteseachgenre(x, y, z) takes three parameters as input, x, y, and z. 
    It plots a bar chart for the number of People votes for each genre in the DataFrame x against the genre column and the corresponding number of votes column.

    Parameters
    ----------
    x : pandas DataFrame
    A DataFrame containing the data to be plotted.
    y : str
    The column name of the genre in the DataFrame.
    z : str
    The column name of the corresponding number of votes in the DataFrame.

    Returns
    -------
    None.
    The function only plots the bar chart and does not return any value.
    The function call in the last line uses the function to plot a bar chart 
    for the number of votes for each genre in the DataFrame best_shows against the MAIN_GENRE column and the corresponding NUMBER_OF_VOTES column.
    """
    # plotting bar graph
    plt.figure(figsize=(20, 10))
    plt.bar(x[y], x[z])
    # labelling
    plt.xlabel("GENRE", fontweight="bold")
    plt.ylabel("Number of people votes", fontweight="bold")
    plt.title("PEOPLE VOTES FOR BEST NETFLIX SHOWS GENRES", fontweight="bold")
    plt.legend()
    # save figure
    plt.savefig("barplot_for_voteseachgenre.png")
    plt.show()


# calling the function barplot_for_voteseachgenre
barplot_for_voteseachgenre(best_shows, "MAIN_GENRE", "NUMBER_OF_VOTES")


def bestshows_genre_piechart(best_shows, column_name):
    """
    The function bestshows_genre_piechart(best_shows, column_name) takes two parameters as input, best_shows and column_name. 
    It counts the unique values in the column column_name of the DataFrame best_shows, and then plots a pie chart with the counts of each unique value.

    Parameters
    ----------
    best_shows : pandas DataFrame
    A DataFrame containing the data to be plotted.
    column_name : str
    The name of the column in the DataFrame for which the pie chart is to be plotted.

    Returns
    -------
    None.
    The function only plots the pie chart and does not return any value.
    The function call in the last line uses the function to plot a pie chart for the MAIN_GENRE column of the DataFrame best_shows. The title of the pie chart is "BEST NETFLIX SHOWS GENRE"
    """
    # plotting pie chart
    value_counts = best_shows[column_name].value_counts()
    labels1 = value_counts.index.tolist()
    counts = value_counts.tolist()
    plt.figure(figsize=(30, 10))
    plt.pie(counts, autopct='%1.1f%%', labels=labels1)
    plt.title("BEST NETFLIX SHOWS GENRE", fontweight="bold")
    plt.legend()
    # save figure
    plt.savefig("bestshows_genre_piechart.png")
    plt.show()


# calling the function bestshows_genre_piechart
bestshows_genre_piechart(best_shows, "MAIN_GENRE")
