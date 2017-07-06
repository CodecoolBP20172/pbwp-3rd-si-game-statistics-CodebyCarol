
# Printing functions
from pprint import pprint
import reports
#importing the definitions of reports

#1 How many games are in the file?
pprint ("In this file there is " + \
str(reports.count_games("game_stat.txt")) + " games")


#2 Is there a game from a given year (year is an int)?
pprint ("There were a game in the given year: " + \
    str(reports.decide('game_stat.txt', 1998)))


#3 Which was the latest game?
pprint ("The latest game was: " + reports.get_latest('game_stat.txt'))


#4 How many games do we have by genre?
pprint ("The answer is: " + \
    str(reports.count_by_genre('game_stat.txt', 'Real-time strategy')))


#5 What is the line number of the given game (by title)?
pprint ("The asked game is in line " + \
    str(reports.get_line_number_by_title('game_stat.txt', 'Half-Life')))
