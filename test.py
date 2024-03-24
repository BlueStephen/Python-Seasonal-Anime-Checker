from jikanpy import Jikan

# Create a Jikan instance
jikan = Jikan()

# Get the current anime season information
season_info = jikan.seasons(extension='now')

# Extract titles from the response
titles = [anime['title'] for anime in season_info['data']]

# Print the titles
for title in titles:
    print(title)
