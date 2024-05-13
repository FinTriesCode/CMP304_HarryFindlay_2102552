'''
Harry Findlay
2102552
'''

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
#from statistics import mean
import UserTesting as tests




#lists used to store classes for playerID's
playerClassificationsAI = {}
playerClassifications = {}

#lists to store summed ammounts of 
totalKillsArr = []
totalAssistsArr = []
totalDeathsArr = []

#function used to classify players into tags depending on how player stats compare to the AI 'rules'
def PlayerClassification(players):

    print("-----Getting highest scoring stats from player's info-----\n")
    for index, row in players.iterrows():

        #iterate through game dataset to get player data
        playerData = row
        filledData = playerData[["KB", "D", "HK"]].fillna(0)

            #kills
        totalKills = filledData["KB"].sum()
        totalKillsArr.append(totalKills)

            #assist
        totalAssists = filledData["HK"]
        totalAssistsArr.append(totalAssists)

            #deaths
        totalDeaths = filledData["D"]
        totalDeathsArr.append(totalDeaths)


    print("-----Config the player data-----")
    for index, row in players.iterrows():

        #loop through data set and get desired player data (kills, assists, deaths)
        playerData = row
        filledData = playerData[["KB", "D", "HK"]].fillna(0)

        #player data
        playerKills = filledData["KB"]
        playerAssists = filledData["HK"]   
        playerDeaths = filledData["D"]

        #set cassification rules
        if playerKills >= 6 and playerDeaths >= 3 and playerDeaths <= 8:
            playerClassifications[index] = "Assault"
        elif playerAssists >= 6 and playerDeaths >= 4:
            playerClassifications[index] = "Team Player"
        elif playerKills <= 7 and playerKills >= 2 and playerDeaths <= 7 and playerAssists >= 2:
            playerClassifications[index] = "Defender"
        elif playerKills >= 1 and playerKills <= 5 and playerDeaths >= 1:
            playerClassifications[index] = "Scout"
        elif playerDeaths >= 1:
            playerClassifications[index] = "Casual Player"

        else:
            playerClassifications[index] = "Not Classified"



    #show the chart
    tests.PieChartsDraw(playerClassifications, players) 


#AI's classification funciton
def PlayerClassificationAI(players):

    #create lists to sort player data
    print("-----AI's player classification-----")
    playerStats = []  
    classNames = []  


    print("-----AI Traing Data Set-----")
    for index, row in players.iterrows():

        #gets the stats per game for each player
        stats = [
            row['KB'],
            row['D'],
            row['HK'],
        ]

        #add stats to AI's knowledge lists of player stats
        playerStats.append(stats)

        #gets the classification of each player from the dictionary created above
        classification = playerClassifications[index]
        print(classification)

        #turns each classification into a numerical value ot allow for easier sorting and outputting
        if classification == "Assault":
            classNames.append(1)
        elif classification == "Team Player":
            classNames.append(2)
        elif classification == "Defender":
            classNames.append(3)
        elif classification == "Scout":
            classNames.append(4)
        elif classification == "Casual Player":
            classNames.append(5)
        else:
            classNames.append(6)

    #split the data into a ratio, turning the data into sub-data sets: training and testing data sets
    print("-----Splitting All AI Data Sets-----")

    X_train, X_test, y_train, y_test = train_test_split(playerStats, classNames, test_size=0.4, random_state=42) #playerStats is the X, classNames is the Y

    #beging AI training process
    print("-----Training AI-----")
    decisionTreeClassifier = DecisionTreeClassifier() #create a new dicision tree for predictions
    decisionTreeClassifier.fit(X_train, y_train) #attach playerStats data and lables to classNames and classifictions data

    #start predicion process
    print("-----Making Predictions-----")
    yPredict = decisionTreeClassifier.predict(X_test) #makes predictions using the x test data (playerStats) and stores the generated labels

    #iterate through AI predicitons and store in new dict.
    print("-----Prediction results being stored-----")
    print(yPredict)
    for index, predict in enumerate(yPredict):  #iterate through all player data
        playerClassificationsAI[index] = predict  #store all prediciotns made next to the appropriate player

    #pie chart to visualise prediction results
    print("-----Displaying classes predicted-----")
    tests.PieChartsDrawAI(playerClassificationsAI, players) 

    #generate accuracy report   
    print("Drawing AI's accuracy chart")
    accuracyReport = classification_report(y_test, yPredict)
    print(accuracyReport)