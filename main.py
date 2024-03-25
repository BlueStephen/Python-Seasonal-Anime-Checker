import tkinter as tk
from jikanpy import Jikan

class AnimeSeasonCheckerApp:
    def __init__(self, master):
        self.master = master
        master.title("Anime Season Checker")

        self.jikan = Jikan()

        # Create labels, entry fields, and buttons for GUI
        self.choice_var = tk.StringVar()
        self.choice_var.set('current')
        self.choices = ['current', 'upcoming', 'specific']
        self.choice_label = tk.Label(master, text="Select season:")
        self.choice_label.pack()
        self.choice_menu = tk.OptionMenu(master, self.choice_var, *self.choices)
        self.choice_menu.pack()

        self.year_label = tk.Label(master, text="Enter the year:")
        self.year_label.pack()
        self.year_entry = tk.Entry(master)
        self.year_entry.pack()

        self.season_label = tk.Label(master, text="Enter the season (spring/summer/winter/fall):")
        self.season_label.pack()
        self.season_entry = tk.Entry(master)
        self.season_entry.pack()

        self.fetch_button = tk.Button(master, text="Fetch Anime", command=self.fetch_seasonal_anime)
        self.fetch_button.pack()

        # Create a listbox to display anime titles
        self.anime_listbox = tk.Listbox(master)
        self.anime_listbox.pack(fill=tk.BOTH, expand=True)

    def fetch_seasonal_anime(self):
        choice = self.choice_var.get()
        if choice == 'current':
            season_info = self.jikan.seasons(extension='now')
        elif choice == 'upcoming':
            season_info = self.jikan.seasons(extension='upcoming')
        elif choice == 'specific':
            year = int(self.year_entry.get())
            season = self.season_entry.get().lower()
            season_info = self.jikan.seasons(year=year, season=season)
        else:
            # Handle invalid choice
            return
        
        self.anime_listbox.delete(0, tk.END)
        if 'data' in season_info:
            titles = [anime['title'] for anime in season_info['data']]
            for title in titles:
                self.anime_listbox.insert(tk.END, title)
        else:
            self.anime_listbox.insert(tk.END, "No anime information found for the selected season.")

def main():
    root = tk.Tk()
    app = AnimeSeasonCheckerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
