from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from statistics import mean
import UserTesting as tests



#dictionary list to store classes against player IDs (the correct one then the predicted one)
playerClassificationsAI = {}
playerClassifications = {}

#lists to store running sums
totalKillsArr = []
totalDeathsArr = []
totalAssistsArr = []

totalKillsNorm = []
totalDeathsNorm = []
totalAssistsNorm = []




def PlayerClassification(players):

    print("-----Getting highest scoring stats from player's info-----\n")
    for playerID, playerData in players:

        filledData = playerData[["KB", "D", "HK"]].fillna(0)

        totalKills = filledData["KB"].sum()
        totalKillsArr.append(totalKills)
        mostKills = max(totalAssistsArr)

        totalAssists = filledData["HK"]
        totalAssistsArr.append(totalAssists)
        mostAssists = max(totalAssistsArr)

        totalDeaths = filledData["D"]
        totalDeathsArr.append(totalDeaths)
        mostDeaths = max(totalDeathsArr)


    print("-----Normalising the player data-----")
    for playerID, playerData in players:

        filledData = playerData[["KB", "D", "HK"]].fillna(0)

        playerKills = filledData["KB"]
        mostKills = filledData["KB"].max()
        normalisedKills = playerKills / mostKills
        totalKillsNorm.append(normalisedKills)

        print(f"Debug:\nplayerKills: {playerKills}\nmostKills: {mostKills}\n")


        playerAssists = filledData["HK"]
        mostAssists = filledData["HK"].max()
        normalisedAssists = playerAssists / mostAssists
        totalAssistsNorm.append(normalisedAssists)        

        print(f"Debug:\nplayerAssists: {playerAssists}\nmostAssists: {mostAssists}\n")


        playerDeaths = filledData["D"]
        mostDeaths = filledData["D"].max()
        normalisedDeaths = playerDeaths / mostDeaths
        totalDeathsNorm.append(normalisedDeaths)

        print(f"Debug:\nplayerDeaths: {playerDeaths}\nmostDeaths: {mostDeaths}\n")


        print("-----Processing data against rules-----")
        for playerID, playerData in players:

            playerKills = filledData["KB"]
            mostKills = filledData["KB"].max()
            normalisedKills = playerKills / mostKills

            playerAssists = filledData["HK"]
            mostAssists = filledData["HK"].max()
            normalisedAssists = playerAssists / mostAssists

            playerDeaths = filledData["D"]
            mostDeaths = filledData["D"].max()
            normalisedDeaths = playerDeaths / mostDeaths


            if normalisedKills[playerID] >= 15:
                playerClassifications[playerID] = "Legendary"
            elif normalisedKills[playerID] >= 10 and normalisedKills[playerID] < 15:
                playerClassifications[playerID] = "Godly"
            elif normalisedKills[playerID] >= 5 and normalisedKills[playerID] < 10:
                playerClassifications[playerID] = "Average"
            elif normalisedKills[playerID] >= 1 and normalisedKills[playerID] < 5:
                playerClassifications[playerID] = "Peasant"
            elif normalisedKills[playerID] == 0 :
                playerClassifications[playerID] = "Dead Weight"
            else:
                playerClassifications[playerID] = "Not Classified"

            
            if normalisedAssists[playerID] >= 25:
                playerClassifications[playerID] = "Setter Upper"
            elif normalisedAssists[playerID] >= 15 and normalisedAssists[playerID] < 25:
                playerClassifications[playerID] = "Wingman"
            elif normalisedAssists[playerID] >= 10 and normalisedAssists[playerID] < 15:
                playerClassifications[playerID] = "Assistee"
            elif normalisedAssists[playerID] >= 5 and normalisedAssists[playerID] < 10:
                playerClassifications[playerID] = "Assist Intern"
            elif normalisedAssists[playerID] >= 1 and normalisedAssists[playerID] < 5:
                playerClassifications[playerID] = "Assist Novice"
            elif normalisedAssists[playerID] == 0 :
                playerClassifications[playerID] = "Kill Hog"
            else:
                playerClassifications[playerID] = "Not Classified"


            if normalisedDeaths[playerID] >= 25:
                playerClassifications[playerID] = "Liability"
            elif normalisedDeaths[playerID] >= 15 and normalisedDeaths[playerID] < 10:
                playerClassifications[playerID] = "Grim Reaper's Favourate"
            elif normalisedDeaths[playerID] >= 10 and normalisedDeaths[playerID] < 5:
                playerClassifications[playerID] = "Average Death"
            elif normalisedDeaths[playerID] >= 5 and normalisedDeaths[playerID] < 10:
                playerClassifications[playerID] = "Death Dodger"
            elif normalisedDeaths[playerID] >= 1 and normalisedDeaths[playerID] < 5:
                playerClassifications[playerID] = "Invincible"
            elif normalisedDeaths[playerID] == 0 :
                playerClassifications[playerID] = "Flawless"
            else:
                playerClassifications[playerID] = "Not Classified"


def PlayerClassificationAI(players):

    print("-----AI's player classification-----")
    playerStats = []  
    classNames = []  


    print("-----AI Traing Data Set-----")
    for playerID, playerData in players:
        #iterate over every row
        for index, row in playerData.iterrows():

            #gets the stats per game for each player
            stats = [
                row['KB'],
                row['D'],
                row['HK'],
            ]

            #add these stats to the AI's knowledge listW of player stats
            playerStats.append(stats)

            #gets the classification of each player from the dictionary created above
            classification = playerClassifications[playerID]

            #turns each class into a value to make it easier for outputting from the AI (essentially works like having an int array instead
            #of a string array)
            if classification == "Legendary":
                classNames.append(1)
            elif classification == "Godly":
                classNames.append(2)
            elif classification == "Average":
                classNames.append(3)
            elif classification == "Peasant":
                classNames.append(4)
            elif classification == "Dead Weight":
                classNames.append(5)

    #split the data into enough to train the AI, then enough to test this learning
    print("-----Splitting All AI Data Sets-----")
    X_train, X_test, y_train, y_test = train_test_split(playerStats, classNames, test_size=0.1, random_state=42) #playerStats is the X, classNames is the Y

    #begin to train the AI
    print("-----Training AI-----")
    decisionTreeClassifier = DecisionTreeClassifier()     #creates a new decision tree classifier for supervised learning
    decisionTreeClassifier.fit(X_train, y_train)   #uses the player stats stored in X and labels attached to these stats in Y to learn the class rules

    #make predictions
    print("-----Making Predictions-----")
    yPredict = decisionTreeClassifier.predict(X_test)     #uses the portion of data stored in x_test to make predictions and stores these labels in y_predict

    #iterate through the AI's predictions and store them in a second dictionary
    print("-----Prediction results being stored-----")
    for i, (playerID, _) in enumerate(players):       #for loop which cycles through all of the players dataset
        playerClassificationsAI[playerID] = yPredict[i]   #stores all predicted classes into dictionary next to correct player ID

    #draws a pie chart displaying how the AI predicted the split of classes
    print("-----Displaying classes predicted-----")
    tests.drawPieChartsAI(playerClassificationsAI, players) 

    #writes out an accuracy report showing where the AI was most and least accurate    
    print("Drawing AI's accuracy chart")
    accuracyReport = classification_report(y_test, yPredict)
    print(accuracyReport)