'''
Harry Findlay
2102552
'''

import pandas
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def ReadData():
    global playerData
    global fillerData

    #read in the dataset using pandas on the specified directory
    playerData = pandas.read_csv("data/wowbgs.csv")

    fillerData = playerData[['KB', 'D', 'HK']].fillna(0) #player kills, deaths, assists

#funciton to calculate the optimal number of clusters, also plots a graph
def ElbowPlot():
    global withinSumOfSquares

    withinSumOfSquares = []
    elbowCheck = 50 #max number of available clusters

    print("-----Calculating data-----\n")

    for i in range(1, elbowCheck + 1):
        kmeans = KMeans(n_clusters=i, random_state=0, n_init="auto").fit(fillerData) 
        withinSumOfSquares.append(kmeans.inertia_)

    print("-----Graph Plotting-----")
    plt.plot(withinSumOfSquares)
    plt.show()

#filter dataset by faction, used to specify/split
def FilterByFaction(faction):
    playerFilteredData = playerData[playerData["Faction"] == faction]

    return playerFilteredData
