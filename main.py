#Harry Findlay
#Player Classification

import DataPreperation as prep
import DataAnalysis as Analysis

prep.readData()     #read in data files

optimalClusters = 150      #decided from elbow graph
elbow = input("Insert 'see' to display graphis\nOther input will skip\n")      #gives user option whether or not to see graph of optimal clusters

#if user inputs a value of one it will show the graph otherwise this step will be skipped
if elbow == "see":
    prep.plotElbow()

region_check = ""   #create a variable to allow user to input a selection
#create a list of valid regions for players to input
valid_regions = ["Oceania", "North America", "South America", "Asia-Pacific North", "Asia-Pacific South", "Middle East & North Africa", 
                 "Europe", "Sub-Saharan Africa"]

while region_check != "Quit":
    print(f"Enter a region from the list: ")
    for region in valid_regions:
        print(region)
    region_check = input("Enter region, or Quit to exit: ")  #user selects which region to extract data from   
    if region_check in valid_regions:
        region_data = prep.selectRegion(region_check)   #select players from a single region
        player_data = region_data.groupby('player_id')      #groups all rows relating to the same player
        matches_played = player_data.size()   #the size of the player_data variable will show how many matches each player participated in - 
                                                #therefore can be useful for averages

        Analysis.classifyPlayers(player_data, matches_played)  #gets max, avg and normalized values for all essential player data
        Analysis.classifyPlayersAI(player_data, matches_played)  #gets max, avg and normalized values for all essential player data

print(f"Closing program...")