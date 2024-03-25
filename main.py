import tkinter as tk
from tkinter import ttk
from jikanpy import Jikan

class AnimeSeasonCheckerApp:
    def __init__(self, master):
        self.master = master
        master.title("Anime Season Checker")

        self.jikan = Jikan()

        # Create labels, entry fields, and buttons for GUI
        self.title_label = tk.Label(master, text="Seasonal Anime Checker", font=("Arial", 16, "bold"))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.choice_var = tk.StringVar()
        self.choice_var.set('current')
        self.choices = ['current', 'upcoming', 'specific']
        self.choice_label = tk.Label(master, text="Select season:")
        self.choice_label.grid(row=1, column=0)
        self.choice_menu = tk.OptionMenu(master, self.choice_var, *self.choices, command=self.update_fields)
        self.choice_menu.grid(row=1, column=1)

        # Create a listbox to display titles
        self.listbox = tk.Listbox(master, height=20, width=40)  # Increase width to 40 and height to 20
        self.listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=10)  # Adjust padding if needed

        # Initially hide the "Enter the year" and "Enter the season" input fields
        self.year_label = tk.Label(master, text="Enter the year:")
        self.year_entry = tk.Entry(master)

        self.season_label = tk.Label(master, text="Enter the season (spring/summer/winter/fall):")
        self.season_entry = tk.Entry(master)

        # Create Fetch Anime button
        self.fetch_button = tk.Button(master, text="Fetch Anime", command=self.fetch_seasonal_anime)
        self.fetch_button.grid(row=6, column=0, columnspan=2)

    def update_fields(self, choice):
        # Remove existing "Enter the year" and "Enter the season" input fields
        self.year_label.grid_forget()
        self.year_entry.grid_forget()
        self.season_label.grid_forget()
        self.season_entry.grid_forget()

        if choice == 'specific':
            # Show "Enter the year" and "Enter the season" input fields for specific option
            self.year_label.grid(row=2, column=0)
            self.year_entry.grid(row=2, column=1)
            self.season_label.grid(row=3, column=0)
            self.season_entry.grid(row=3, column=1)

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
        
        # Clear existing items in the listbox
        self.listbox.delete(0, tk.END)
        
        if 'data' in season_info:
            titles = [anime['title'] for anime in season_info['data']]
            for title in titles:
                # Insert title into the listbox
                self.listbox.insert(tk.END, title)
        else:
            self.listbox.insert(tk.END, "No anime information found for the selected season.")

def main():
    root = tk.Tk()
    app = AnimeSeasonCheckerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
