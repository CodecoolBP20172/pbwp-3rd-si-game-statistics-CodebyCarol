# Report functions
# 2nd part


def list_of_games(file_name):
    with open(file_name, 'r') as text:
        list_of_games = []
        for line in text:
            game = line.split('\t')
            list_of_games.append(game)
    return list_of_games


def count_games(file_name):
    with open(file_name, 'r') as text:
        return len(text.readlines())


# 1: What is the title of the most played game?(i.e. sold the most copies)
def get_most_played(file_name):
    text = list_of_games(file_name)
    max_sold = 0.00
    for line in text:
        game_name = name_index = line[0]
        total_sold_index = line[1]
        if float(max_sold) == float(total_sold_index):
            return game_name
        if float(max_sold) < float(total_sold_index):
            max_sold = total_sold_index
            game_name = name_index
        return game_name  # check this with different order!! not sure..
    # if there is more than one, than returns the first from the file


# 2: How many copies have been sold total?
def sum_sold(file_name):
    text = list_of_games(file_name)
    sum_sold = 0.00
    for line in text:
        sum_sold += float(line[1])
    return sum_sold
    # number


# 3: What is the overage selling?
def get_selling_avg(file_name):
    lines = count_games(file_name)
    text = list_of_games(file_name)
    sum_sold = 0.00
    for line in text:
        sum_sold += float(line[1])
    average = sum_sold/lines
    return (average)
    # number


# 4: How many characters long is the longest title?
def count_longest_title(file_name):
    title_lenght = 1
    text = list_of_games(file_name)
    for line in text:
        title_index = line[0]
        if title_lenght < len(title_index):
            title_lenght = len(title_index)
    return title_lenght
    # number


# 5: What is the average of the release dates?
def get_date_avg(file_name):
    text = list_of_games(file_name)
    lines = count_games(file_name)
    sum_date = 0
    for line in text:
        date_index = line[2]
        sum_date += int(date_index)
    date_avg = round(sum_date/lines)
    return date_avg
    # average year (number) rounded up


# 6: What properties has a game?
def get_game(file_name, title):
    text = list_of_games(file_name)
    for line in text:
        title_index = line[0]
        total_sold_index = float(line[1])
        release_date_index = int(line[2])
        genre_index = line[3]
        publisher_index = line[4].replace('\n', '')
        if title == title_index:
            list_of_properties = [title_index, total_sold_index,
                                  release_date_index, genre_index,
                                  publisher_index]
            return list_of_properties
            # list of all properties of the game (list of various type)
#the nice to have parts under developing    
