import random
import csv
import datetime


with open('things.csv', mode='r') as infile:
    reader = csv.reader(infile)
    Items = list(reader)


Items = [[item[0], float(item[1])] for item in Items]


playAgain = True


while playAgain:

    matchUpNotChosen = True

    while matchUpNotChosen:
        Indexes = random.sample(range(0, len(Items)), 2)

        item1Index = Indexes[0]
        item2Index = Indexes[1]

        matchUpNotChosen = False


    print("\n Which is more Right Wing? \n \n" + Items[item1Index][0] + " or " + Items[item2Index][0] + "\n")

    item1elo = float(Items[item1Index][1])
    item2elo = float(Items[item2Index][1])
    K = 40

    expectedWin1 = 1 /(1 + pow(10, (item2elo - item1elo)/400))

    #print("Chance of a " +  Items[item1Index][0] + " Win is: " + str(expectedWin1))


    expectedWin2 = 1 /(1 + pow(10, (item1elo - item2elo)/400))

    #print("Chance of a " +  Items[item2Index][0] + " Win is: " + str(expectedWin2))

    inputneeded = True
    while inputneeded:
        userInput = input("Type '1' for " + Items[item1Index][0] + ". Type '2' for " + Items[item2Index][0] + "\n")
        print("\n")

        if userInput == "1":

            item1Score = 1
            item2Score = 0
            inputneeded = False
            print(Items[item1Index][0] + " Wins!!")


        elif userInput == "2":
            item1Score = 0
            item2Score = 1
            inputneeded = False
            print(Items[item2Index][0] + " Wins!!")

        else:
            print("Incorrect input, try again")


    item1elo = item1elo + K*( item1Score- expectedWin1)

    item1eloChange = K*( item1Score - expectedWin1)

    if item1Score == 0:
        sign = ""
    else:
        sign = "+"

    print(Items[item1Index][0] + " Elo: " + str(round(item1elo,0)) + " (" + sign + str(round(item1eloChange,0)) + ")")


    item2elo = item2elo + K*(item2Score - expectedWin2)

    item2eloChange = K*(item2Score - expectedWin2)

    if item2Score == 0:
        sign = ""
    else:
        sign = "+"

    print(Items[item2Index][0] + " Elo: " + str(round(item2elo,0)) + " (" + sign + str(round(item2eloChange,0)) + ")")

    Items[item1Index][1] = item1elo
    Items[item2Index][1] = item2elo

    # Open file to write data
    with open('things.csv', 'w', newline='') as file:
        writer = csv.writer(file)


    # Write each inner list as a new row
        writer.writerows(Items)

    Userplayagain = input("Play again? y/n")
    if Userplayagain == "n" :
        print("Goodbye \n Current Right Wing Rankings\n")
        def myFunc(e):
            return e[1]
        Items.sort(reverse=True, key=myFunc)
        for i in Items :
            print(str(i[0]) + " - Elo: " + str(round((i[1]),2)))
            #str(round(answer, 2))
        playAgain = False
        print("\n")

    else:
        print("Lets Go!! \n")
