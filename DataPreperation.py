import pandas
import matplotlib as plt
from sklearn.cluster import KMeans

def ReadData():
    global playerData
    global fillerData

    #read in the file and use pandas to read the csv
    playerCSVData = "data/wowbgs"
    playerData = pandas.read_csv(playerCSVData)

    fillerData = playerData[['KB', 'D', 'HK']].fillna(0) #player gender, player age, character class{es}, character race(s)

def FilterByGender(gender):
    playerFilteredData = playerData[playerData['Gender']]

    return playerFilteredData

def ElbowPlot():
    global withinSumOfSquares

    withinSumOfSquares = []
    elbowCheck = 150 #ax num of clusters

    print("-----Calculating data-----\n")

    for i in range(1, elbowCheck + 1):
        kmeans = KMeans(n_clusters=i, random_state=0, n_init="auto").fit(fillerData) 
        withinSumOfSquares.append(kmeans.inertia_)

    print("-----Graph Plotting-----")
    plt.plot(withinSumOfSquares)
    plt.show()

