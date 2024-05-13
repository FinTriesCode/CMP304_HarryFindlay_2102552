'''
Player Classification
Harry Findlay
2102552
'''

import DataPreperation
import DataAnalysis

DataPreperation.ReadData() #read in data drom DataPreperation

optimalClusters = 50      #decided from elbow graph
elbow = input("Insert 'see' to display graphis\nOther input will skip\n")      #gives user option whether or not to see graph of optimal clusters

#if user inputs a value of one it will show the graph otherwise this step will be skipped
if elbow == "see":
    DataPreperation.ElbowPlot()

factionInput = ""   #create a variable to allow user to input a selection

while factionInput != "Quit":
    factionInput = input("Enter Faction ('Horde' or 'Alliance') to classify.\nType 'Quit' to exit\nInput: ")  #user selects which region to extract data from
    if factionInput == "Alliance" or factionInput == "Horde":
        factionData = DataPreperation.FilterByFaction(factionInput)   #select players from a single region

        DataAnalysis.PlayerClassification(factionData)  #gets max, avg and normalized values for all essential player data
        DataAnalysis.PlayerClassificationAI(factionData)  #gets max, avg and normalized values for all essential player data

print(f"Closing program...")