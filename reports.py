# How many games are in the file?
def count_games(file_name):
    with open ('game_stat.txt', 'r') as text:
        return len(text.readlines())
        #expected return: number


#Is there a game from a given year?
def decide(file_name, year):
    if type(year) is not int:
        raise TypeError
    with open ('game_stat.txt', 'r') as text:
        for game in text:
            data = game.split("\t")
            release_year_index = 2
            release_year = int(data[release_year_index])
            if release_year == year:
                return True
        return False
        #expected return: boolean value


#Making one big list, with list of games(lines)
def make_list_of_games(file_name):
    with open ('game_stat.txt', 'r') as text:
        all_game_list=[]
        latest = "0"
        for line in text:
            game = line.split('\t')
            all_game_list.append(game)
    return all_game_list


#Which was the latest game?
def get_latest(file_name):
    text = make_list_of_games(file_name)
    latest = 0
    for line in text:
        name_index = line[0]
        year_index = line[2]
        if int(year_index) > int(latest):
            latest = year_index
            latest_game = name_index
    return latest_game
#expected return: title of the latest game, as string


#How many games do we have by genre?
def count_by_genre(file_name, genre):
    text = make_list_of_games(file_name)
    count = 0
    for line in text:
        genre_index = line[3]
        if genre_index == genre:
            count +=1
    return count
#expected return: a number


#What is the line number of the given game (by title)?
def get_line_number_by_title(file_name, title):
    text = make_list_of_games(file_name)
    line_number = 1
    for line in text:
        title_index = line[0]
        if title_index == title:
            return line_number
        line_number += 1

    #expected return: a number
    #(if there is no game found, then raises ValueError exception)

"""
Nice to have:
"""
# What is the alfabetical ordered list of the titles?
def sort_abc(file_name):
    pass
    #expected return: a list of strings WITHOUT built in sort()
    #or (sorted) functions

#What are the genres?
def get_genres(file_name):
    pass
    #Expected output of the function: a list of the genres (without duplicates,
    #in alphabetical order)

#What is the release date of the top sold "First-person shooter" game?
def  when_was_top_sold_fps(file_name):
    pass
    #year of the release, as integer
    #(if there is no game with genre "First-person shooter"
    #then raises ValueError exception
