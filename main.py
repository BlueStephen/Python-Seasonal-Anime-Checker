from jikanpy import Jikan
jikan = Jikan()

print("Welcome to my Anime Season Checker, where you can check which anime are airing for a specific season.")
print("To begin, select if you would like to check the current, upcoming, or a specific season.")

# Ask the user for their choice
choice = input("Enter 'current', 'upcoming', or 'specific': ").lower()

if choice == 'current':
    season_info = jikan.seasons(extension='now')
elif choice == 'upcoming':
    season_info = jikan.seasons(extension='upcoming')
elif choice == 'specific':
    year = int(input("Enter the year: "))
    season = input("Enter the season (spring/summer/winter/fall): ").lower()
    season_info = jikan.seasons(year=year, season=season)
else:
    print("Invalid choice. Please enter 'current', 'upcoming', or 'specific'.")

if 'data' in season_info:
    # Extract titles from the response
    titles = [anime['title'] for anime in season_info['data']]
    
    # Print the titles
    print("\nAnime titles for the selected season:")
    for title in titles:
        print(title)
else:
    print("No anime information found for the selected season.")