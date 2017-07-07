# Printing functions
from pprint import pprint
import reports

#1: What is the title of the most played game?(i.e. sold the most copies)
pprint('The most played game is: '  + \
reports.get_most_played('game_stat.txt') )


#2: How many copies have been sold total?
pprint('The total number of sold copies: ' + \
    str(reports.sum_sold('game_stat.txt')) + ' million')

#3: What is the overage selling?
pprint('The overage saled copies is ' + \
    str('%.2f' % reports.get_selling_avg('game_stat.txt')) + ' million')


#4: How many characters long is the longest title?
pprint('The longest title has: ' + \
    str(reports.count_longest_title('game_stat.txt')) + ' characters')

#5: What is the average of the release dates?
pprint(str(reports.get_date_avg('game_stat.txt')) + \
    ' is the average release date of this games') 

#6: What properties has a game?
pprint('The Minecraft game has the following properties: ' + \
    str(reports.get_game('game_stat.txt', 'Minecraft')))
