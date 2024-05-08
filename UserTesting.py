import matplotlib.pyplot as plt

#draws pie chart for manual classification
def PieChartsDraw(classes, dataset):
    #default vars which will decide size of each section
    Legendary = 0 
    Godly = 0
    Average = 0
    Peasant = 0
    DeadWeight = 0
    other = 0
    

    #iterate through the classes dictionary
    for player_id, playerData in dataset:

        #get the class string from each player ID
        classification = classes[player_id]

        #add one to the counter of the appropriate class as it is found in dictionary
        if classification == "Legendary":
            Legendary += 1
        elif classification == "Godly":
            Godly += 1
        elif classification == "Average":
            Average += 1
        elif classification == "Peasant":
            Peasant += 1
        elif classification == "Dead Weight":
            DeadWeight += 1
        else:
            other += 1

    #define labels for each section
    labels = "Legendary", "Godly", "Average", "Peasant", "Dead Weight", "Undefined"

    #use the counters to correctly size each section next to their labels
    sizes = [Legendary, Godly, Average, Peasant, DeadWeight, other]

    #create the pie chart
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct="%1.1f%%")    #uses sizes and labels lists from above, autopct rounds each section to 1dp

    #display
    plt.show()

#draws pie chart for AI classification
def PieChartsDrawAI(classes, dataset):
    #all is exactly the same as the function above, except the first iterator works slightly differently
    Legendary = 0 
    Godly = 0
    Average = 0
    Peasant = 0
    DeadWeight = 0
    other = 0

    for player_id, player_data in dataset:
        classification = classes[player_id]
        #largely the same as above, however since the AI is using integers to store class with each ID, it must check which integer
        #is found in each iteration instead of which string, could have been done in same function but this way is more maintainable
        if classification == 1:
            Legendary += 1
        elif classification == 2:
            Godly += 1
        elif classification == 3:
            Average += 1
        elif classification == 4:
            Peasant += 1
        elif classification == 5:
            DeadWeight += 1
        elif classification == 6:
            other += 1
        else:
            others += 1

    labels = "Legendary", "Godly", "Average", "Peasant", "Dead Weight", "Undefined"
    sizes = [Legendary, Godly, Average, Peasant, DeadWeight, other]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%')

    plt.show()