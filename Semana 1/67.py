name = input("Please enter your name:")
facebook = float(input("How many hours do you spend on Facebook?"))
fifa = float(input("How many hours do you spend on fifa?:"))
x = float(input("How many hours do you spend on x?:"))
disney+ = float(input("How many hours do you spend on Disney+?:"))
spotify = float(input("How many hours do you spend on Spotify?:"))
total_hours = facebook + fifa + x + disney+ + spotify
percentage_per_day = (total_hours / 24) * 100
print("Username:", name)
print("Total hours spent on media:", total_hours)
print("Percentage of day spent on media:", percentage_per_day)