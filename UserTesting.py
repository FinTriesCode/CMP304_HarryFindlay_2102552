import matplotlib.pyplot as plt

#draws pie chart for manual classification
def PieChartsDraw(classes, dataset):
    #default vars which will decide size of each section
    Assault = 0 
    TeamPlayer = 0
    Defender = 0
    Scout = 0
    CasualPlayer = 0
    other = 0
    

    #iterate through the classes dictionary
    for index, row in dataset.iterrows():

        #get the class string from each player ID
        classification = classes[index]

        #add one to the counter of the appropriate class as it is found in dictionary
        if classification == "Assault":
            Assault += 1
        elif classification == "Team Player":
            TeamPlayer += 1
        elif classification == "Defender":
            Defender += 1
        elif classification == "Scout":
            Scout += 1
        elif classification == "Casual Player":
            CasualPlayer += 1
        else:
            other += 1

    #define labels for each section
    labels = "Assault", "Team Player", "Defender", "Scout", "Casual Player", "Undefined"
    sizes = [Assault, TeamPlayer, Defender, Scout, CasualPlayer, other]

    #create the pie chart
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct="%1.1f%%")    #uses sizes and labels lists from above, autopct rounds each section to 1dp

    #display
    plt.show()

#draws pie chart for AI classification
def PieChartsDrawAI(classes, dataset):
    #all is exactly the same as the function above, except the first iterator works slightly differently
    Assault = 0 
    TeamPlayer = 0
    Defender = 0
    Scout = 0
    CasualPlayer = 0
    other = 0

    for index in range(0, len(classes)):
        classification = classes[index]
        #largely the same as above, however since the AI is using integers to store class with each ID, it must check which integer
        #is found in each iteration instead of which string, could have been done in same function but this way is more maintainable
        if classification == 1:
            Assault += 1
        elif classification == 2:
            TeamPlayer += 1
        elif classification == 3:
            Defender += 1
        elif classification == 4:
            Scout += 1
        elif classification == 5:
            CasualPlayer += 1
        elif classification == 6:
            other += 1
        else:
            others += 1

    labels = "Assault", "Team Player", "Defender", "Scout", "Casual Player", "Undefined"
    sizes = [Assault, TeamPlayer, Defender, Scout, CasualPlayer, other]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%')

    plt.show()