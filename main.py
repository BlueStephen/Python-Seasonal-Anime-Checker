from jikanpy import Jikan
jikan = Jikan()

print("Welcome to my Anime Season Checker, where you can check on which anime are airing for a spefic season")
print("To begin, select if you would like to check the current/future/or a specific season")
season_choice = input("Now/Upcoming/Specific: ").lower()
# Get the current anime season information
season_info = jikan.seasons(extension= season_choice, parameters={'filter': 'tv'})

# Extract titles from the response
titles = [anime['title'] for anime in season_info['data']]

# Print the titles
for title in titles:
    print(title)
