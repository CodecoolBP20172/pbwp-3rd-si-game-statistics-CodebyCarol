# Printing functions
from pprint import pprint
import reports
#1: What is the title of the most played game?(i.e. sold the most copies)
reply1 = ('The most played game is: '+ reports.get_most_played('game_stat.txt'))

#2: How many copies have been sold total?
reply2 = ('The total number of sold copies: ' + \
    str(reports.sum_sold('game_stat.txt')) + ' million')

#3: What is the overage selling?
reply3 = ('The overage saled copies is ' + \
    str('%.2f' % reports.get_selling_avg('game_stat.txt')) + ' million')

#4: How many characters long is the longest title?
reply4 = ('The longest title has: ' + \
    str(reports.count_longest_title('game_stat.txt')) + ' characters')

#5: What is the average of the release dates?
reply5 = (str(reports.get_date_avg('game_stat.txt')) + \
    ' is the average release date of this games')

#6: What properties has a game?
reply6 = ('The Minecraft game has the following properties: ' + \
    str(reports.get_game('game_stat.txt', 'Minecraft')))

replies = [reply1, reply2, reply3, reply4, reply5, reply6]

pprint(print('\n'.join (replies)))
