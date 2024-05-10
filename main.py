#Harry Findlay
#Player Classification

import DataPreperation as prep
import DataAnalysis as Analysis

prep.ReadData()     #read in data files

optimalClusters = 50      #decided from elbow graph
elbow = input("Insert 'see' to display graphis\nOther input will skip\n")      #gives user option whether or not to see graph of optimal clusters

#if user inputs a value of one it will show the graph otherwise this step will be skipped
if elbow == "see":
    prep.ElbowPlot()

factionInput = ""   #create a variable to allow user to input a selection

while factionInput != "Quit":
    factionInput = input("Enter Faction ('Horde' or 'Alliance') to classify.\nType 'Quit' to exit\nInput: ")  #user selects which region to extract data from
    if factionInput == "Alliance" or factionInput == "Horde":
        factionData = prep.FilterByFaction(factionInput)   #select players from a single region

        Analysis.PlayerClassification(factionData)  #gets max, avg and normalized values for all essential player data
        Analysis.PlayerClassificationAI(factionData)  #gets max, avg and normalized values for all essential player data

print(f"Closing program...")