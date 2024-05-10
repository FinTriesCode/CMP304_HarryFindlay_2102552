from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from statistics import mean
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


    print("-----Normalising the player data-----")
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

        #add these stats to the AI's knowledge listW of player stats
        playerStats.append(stats)

        #gets the classification of each player from the dictionary created above
        classification = playerClassifications[index]
        print(classification)

        #turns each class into a value to make it easier for outputting from the AI (essentially works like having an int array instead
        #of a string array)
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

    #split the data into enough to train the AI, then enough to test this learning
    print("-----Splitting All AI Data Sets-----")

    X_train, X_test, y_train, y_test = train_test_split(playerStats, classNames, test_size=0.5, random_state=42) #playerStats is the X, classNames is the Y

    #begin to train the AI
    print("-----Training AI-----")
    decisionTreeClassifier = DecisionTreeClassifier()     #creates a new decision tree classifier for supervised learning
    decisionTreeClassifier.fit(X_train, y_train)   #uses the player stats stored in X and labels attached to these stats in Y to learn the class rules

    #make predictions
    print("-----Making Predictions-----")
    yPredict = decisionTreeClassifier.predict(X_test)     #uses the portion of data stored in x_test to make predictions and stores these labels in y_predict

    #iterate through the AI's predictions and store them in a second dictionary
    print("-----Prediction results being stored-----")
    print(yPredict)
    for index, predict in enumerate(yPredict):       #for loop which cycles through all of the players dataset
        playerClassificationsAI[index] = predict  #stores all predicted classes into dictionary next to correct player ID

    #draws a pie chart displaying how the AI predicted the split of classes
    print("-----Displaying classes predicted-----")
    tests.PieChartsDrawAI(playerClassificationsAI, players) 

    #writes out an accuracy report showing where the AI was most and least accurate    
    print("Drawing AI's accuracy chart")
    accuracyReport = classification_report(y_test, yPredict)
    print(accuracyReport)