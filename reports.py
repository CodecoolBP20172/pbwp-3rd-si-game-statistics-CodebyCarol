
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
        #else has been added after test passed
        #expected return: boolean value


#Which was the latest game?
def get_latest(file_name):
    pass
#expected return: title of the latest game, as string

#How many games do we have by genre?
def count_by_genre(file_name, genre):
    pass
#expected return: a number

#What is the line number of the given game (by title)?
def get_line_number_by_title(file_name, title):
    pass
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
