######################################################################
# Program: Football League Table System                              #
# Author:                                                            #
######################################################################
# Description:                                                       #
#                                                                    #
######################################################################

##################
# Import Modules #
##################

import copy

####################
# Global Variables #
####################

# Each team is a dictionary containing a string 'name' and integer values for
# 'points', games 'played', goal scored 'gs', goals conceded 'gc', and games 'won'
emptyTeam = { "name": "" , "points": 0, "played":0, "gs": 0, "gc": 0, "won": 0 }

# The stats for all teams are stored in the 'teams' variable
teams = {}

# The games list holds each game as a list that contains two string elements
# The first string element contains the team i.d.'s separated by a ':'
# The first team in the first string is the 'home' team, the second is the away team
# The second string in a game inner list contains the score separated by a ':'
# The first score is for the home team and the second is for the away team
games = [   ["5:2", "1:0"],
            ["3:4", "1:0"],
            ["1:2", "1:1"],
            ["4:5", "1:0"]
        ]

########################
# Function Definitions #
########################

############################################################
# Function: setupResetTeams()                              #
# Author: Andy Symons &                                    #
############################################################
# Description: This function sets up or resets the 'teams' #
# dictionary of dictionaries to a start of season          #
# initialisation                                           #
############################################################
# Parameters: No parameters                                #
############################################################
# Return Value: No return value                            #
############################################################
def setupResetTeams():
    # For each team from 1 through 5
    # A 'for' loop is used here rather than a while loop as this is a counting scenario
    for i in range(1, 6):
        # copy the 'emptyTeam' to the teams dictionary using the key integer 'i'
        teams[i] = copy.deepcopy(emptyTeam)
        # Set the name of the team to 'Team ' plus the string cast of the integer 'i'
        teams[i]["name"] = "Team " + str(i)

############################################################
# Function: sortTeams                                      #
# Author: A. Symons                                        #
############################################################
# Description: This function sorts the team index into     #
# descending order based upon an order parameter           #
############################################################
# Parameters: index: A list containing integers in an      #
#                    initial order                         #
#             order: An integer indicating which team      #
#                    variable is used to base the order on #
############################################################
# Return Value: A list containing the index list in its    #
# new order                                                #
############################################################
def sortTeams(index, order):

    # for each item in list up to second to last item
    # A for loop is utilised here and not a while loop, as this is a counting scenario
    for i in range(0, len(index) - 1):
        # for each item in list starting at 'i' plus one, up to last item
        # A for loop is utilised here and not a while loop, as this is a counting scenario
        for j in range(i+1, len(index)):
            # Set the values used to sort to zero
            iVal = 0
            jVal = 0
            # A if-elif-else selection construct is used here as there are three options
            # If option is '1', order based on the 'points'
            if order == 1:
                iVal = teams[index[i]]["points"]
                jVal = teams[index[j]]["points"]
            # if option is '2', order based on 'goal difference'
            elif order == 2:
                # Calculate the goal difference for team 'i' and team 'j'
                iVal = teams[index[i]]["gs"] - teams[index[i]]["gc"]
                jVal = teams[index[j]]["gs"] - teams[index[j]]["gc"]
            # Else, the order is '3' and ordered based on games 'won'
            else:
                iVal = teams[index[i]]["won"]
                jVal = teams[index[j]]["won"]
            
            # A simple 'if' selection statement is used here as there is only one selective code block
            # if the value for team 'i' is less than the value for team 'j'
            if iVal < jVal:
                # Swap the index values at indexes 'i' and 'j'
                index[i], index[j] = index[j], index[i]
    
    # Return the re-ordered list
    return index

def sortedTeams():
    # Create an initial index from 1 to number of teams
    teamOrder = [x for x in range(1, len(teams) + 1)]
    # Sort index based on games 'won'
    teamOrder = sortTeams(teamOrder, 3)
    # Sort index based on 'goal difference'
    teamOrder = sortTeams(teamOrder, 2)
    # Sort index based on 'points'
    teamOrder = sortTeams(teamOrder, 1)

    return teamOrder

############################################################
# Function: displayTable                                   #
############################################################
# Description                                              #
#                                                          #
############################################################
# Parameters: index is the order the teams should be       #
#             displayed in                                 #
############################################################
# Return Value: No return value                            #
#                                                          #
############################################################
def displayTable(index):

    print("Team Name    Games Played   Points   Goal Difference   Games Won")    
    print("----------------------------------------------------------------")
    for i in range(0, len(index)):
        print('{0:10} {1:>12} {2:>8} {3:>15} {4:>12}'.format(teams[index[i]]["name"], teams[index[i]]["played"], teams[index[i]]["points"], teams[index[i]]["gs"] - teams[index[i]]["gc"], teams[index[i]]["won"],i, teams[index[i]]["gs"], teams[index[i]]["gc"]))

def displayGames():
    for i in range(0, len(games)):
        print(games[i])

def checkTeamId(teamId, homeTeamId):
    if teamId < 1 or teamId > len(teams):
        print('The team id {0} could not be found.'.format(teamId))
        return 0
    elif teamId == homeTeamId:
        print('The team id {0} is the same as the home team.'.format(teamId))
        return 0
    else:
        return teamId

def getHomeAndAwayTeamIds():
    homeTeamId = 0
    awayTeamId = 0
    while homeTeamId == 0:
        homeTeamId = checkTeamId(getInteger("Enter the home team ID: "), 0)
    while awayTeamId == 0:
        awayTeamId = checkTeamId(getInteger("Enter the away team ID: "), homeTeamId)
    return('{0}:{1}'.format(homeTeamId,awayTeamId))

def getScores():
    homeScore = -1
    awayScore = -1
    while homeScore < 0:
        homeScore = getInteger("Enter the home score: ")
    while awayScore < 0:
        awayScore = getInteger("Enter the away score: ")
    return('{0}:{1}'.format(homeScore,awayScore)) 

def getInteger(message):
    val = input(message)
    while not val.isdigit():
        val = input("'{0}' is not a valid number :".format(val))
    return int(val)

def findGame(teamsIdString):
    for i in range(0, len(games)):
        if games[i][0] == teamsIdString:
            return games[i]
    return ""

def addNewGame():
    matchTeams = getHomeAndAwayTeamIds()
    game = findGame(matchTeams)
    if game != "":
        print("The match {0} has already been entered.".format(game))
        return 0
    score = getScores()
    games.append([matchTeams, score])

def editGame():
    matchTeams = getHomeAndAwayTeamIds()
    game = findGame(matchTeams)
    if game == "":
        print("The match {0} has not been entered.".format(game))
        return 0
    if input("Do you want to edit the teams IDs :").upper() == "Y":
        newTeams = getHomeAndAwayTeamIds()
        newGame = findGame(newTeams)
        if newGame != "":
            print("The match {0} has already been entered.".format(newGame[0]))
            return 0
        if newTeams != "":
            game[0] = newTeams
    else:
        game[1] = getScores()


def processGame(game):

    #print(game[0] , game[1])
    homeTeamId = int(game[0].split(':')[0])
    awayTeamId = int(game[0].split(':')[1])
    homeGoals = int(game[1].split(':')[0])
    awayGoals = int(game[1].split(':')[1])

    #print(homeTeamId,awayTeamId,homeGoals,awayGoals)
    teams[homeTeamId]["played"] +=1
    teams[awayTeamId]["played"] +=1

    if homeGoals > awayGoals:
        teams[homeTeamId]["points"] += 3
        teams[homeTeamId]["won"] += 1
    elif awayGoals > homeGoals:
        teams[awayTeamId]["points"] += 3
        teams[awayTeamId]["won"] += 1
    else:
        teams[homeTeamId]["points"] += 1
        teams[awayTeamId]["points"] += 1

    teams[homeTeamId]["gs"] += homeGoals
    teams[awayTeamId]["gs"] += awayGoals
    
    teams[homeTeamId]["gc"] += awayGoals
    teams[awayTeamId]["gc"] += homeGoals

def resetScores():
    for i in range(1, len(teams)):
        teams[i]["points"]=0
        teams[i]["played"]=0
        teams[i]["won"]=0
        teams[i]["gs"]=0
        teams[i]["gc"]=0
       
def processGames():
    #resetScores()
    for i in range(0, len(games)):
        processGame(games[i])

def getMainMenuOption():
    options = ['1','2','q','Q']
    choice = ''
    print ("""
    Main Menu:        
        1: View League Table
        2: Manage Games
        Q: Quit
    Please enter your choice:""")
    while not choice in options:
        choice = input().upper()
    return choice

def getManageGamesMenuOption():
    displayGames()
    options = ['1','2','b','B']
    choice = ''
    print("""
    Manage Games Sub-menu
        1: Add a Game Result
        2: Edit a Game Result
        B: Back to Main Menu
    Please enter your choice:""")
    while not choice in options:
        choice = input().upper()
    return choice

def mainMenu():
    menuChoice=''
    while menuChoice != 'Q':
        menuChoice = getMainMenuOption()
        if menuChoice == '1':
            processGames()
            displayTable(sortedTeams())
        elif menuChoice == '2':
            manageGamesMenu()

def manageGamesMenu():
    menuChoice = ''
    while menuChoice != 'B':
        menuChoice = getManageGamesMenuOption()
        
        print('menuChoice {0}'.format(menuChoice))    
        if menuChoice == '1':
            addNewGame()
        elif menuChoice == '2':
            editGame()


################
# Main Section #
################

# Call the setupResetTeams() function to initialise the 'teams' dictionary of dictionaries
setupResetTeams()
mainMenu()
