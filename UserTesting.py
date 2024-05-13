'''
Harry Findlay
2102552
'''

import matplotlib.pyplot as plt

#generate pie charts for the ',manual' classifications
def PieChartsDraw(classes, dataset):
    #variables defined to be incremented accordingly. These will be used to create a list later on.
    Assault = 0 
    TeamPlayer = 0
    Defender = 0
    Scout = 0
    CasualPlayer = 0
    other = 0
    

    #iterate thorugh each row in the data set
    for index, row  in dataset.iterrows():

        #get the class label from each row in te data set
        classification = classes[index]

        #increment accordingly
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

    #initialise labels/tags
    labels = "Assault", "Team Player", "Defender", "Scout", "Casual Player", "Undefined"
    sizes = [Assault, TeamPlayer, Defender, Scout, CasualPlayer, other]

    #plot and generate piechart
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct="%1.1f%%")    #uses sizes and labels lists from above, autopct rounds each section to 1dp
    plt.show()

#generate pie chart using MLAI's classifications
def PieChartsDrawAI(classes, dataset):

    '''
    all comments in this function are the same as the funcitons found within PieChartsDraw(classes, dataset)
    any notable changes will be included as comments wihtin this funciton
    '''

    Assault = 0 
    TeamPlayer = 0
    Defender = 0
    Scout = 0
    CasualPlayer = 0
    other = 0

    for index in range(0, len(classes)):
        classification = classes[index]
        
        #uses the integeral value that the data was assigned previously to sort, intead of tags or labels
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