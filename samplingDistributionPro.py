import csv
import pandas as pd
import statistics
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go

df=pd.read_csv("medium_data.csv")
articles=df["reading_time"].to_list()

def randomMean(counter):
    dataSet=[]
    for i in range (0,counter):
        randIndex=random.randint(0,len(articles)-1)
        value=articles[randIndex]
        dataSet.append(value)
    mean=statistics.mean(dataSet)
    return mean

def showFig(meanList):
    df=meanList
    mean=statistics.mean(df)
    fig=ff.create_distplot([df],["reading_time"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="mean"))
    fig.show()

def setup():
    meanList=[]
    for i in range(0,1000):
        set_of_means=randomMean(100)
        meanList.append(set_of_means)
    showFig(meanList)
    mean=statistics.mean(meanList)
    print("mean of sampling distribution: ",mean)

setup()

def standard_deviation():
    meanList=[]
    for i in range(0,1000):
        set_of_means=randomMean(100)
        meanList.append(set_of_means)
        std_deviation=statistics.stdev(meanList)
        print("standard deviation of sampling distribution : ",std_deviation)