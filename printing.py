
# Printing functions
import reports
#importing the definitions of all replies (1-5)

# How many games are in the file?
print ("In this file there is " + \
    str(reports.count_games("game_stat.txt")) + " games")


#Is there a game from a given year (year is an int)?
print (reports.decide('game_stat.txt', 1998))
