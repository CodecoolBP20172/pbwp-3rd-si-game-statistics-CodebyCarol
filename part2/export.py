# Export functions
import reports
reply1 = ('The most played game is: '+ reports.get_most_played('game_stat.txt'))
reply2 = ('The total number of sold copies: ' + \
    str(reports.sum_sold('game_stat.txt')) + ' million')

reply3 = ('The overage saled copies is ' + \
    str('%.2f' % reports.get_selling_avg('game_stat.txt')) + ' million')

reply4 = ('The longest title has: ' + \
    str(reports.count_longest_title('game_stat.txt')) + ' characters')

reply5 = (str(reports.get_date_avg('game_stat.txt')) + \
    ' is the average release date of this games')

reply6 = ('The Minecraft game has the following properties: ' + \
    str(reports.get_game('game_stat.txt', 'Minecraft')))

replies = [reply1, reply2, reply3, reply4, reply5]

with open ('export.txt', 'w') as txt:
    txt.write('\n'.join(replies))
