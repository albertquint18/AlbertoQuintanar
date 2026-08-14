name = input("Please enter your name:")
instagram = float(input("How many hours do you spend on Instagram?"))
messenger = float(input("How many hours do you spend on Messenger?:"))
Netflix = float(input("How many hours do you spend on Netflix?:"))
Dead_by_daylight = float(input("How many hours do you spend on Dead by Daylight?:"))
discord = float(input("How many hours do you spend on Discord?:"))
total_hours = instagram + messenger + Netflix + Dead_by_daylight + discord
percentage_per_day = (total_hours / 24) * 100
print("Username:", name)
print("Total hours spent on media:", total_hours)
print("Percentage of day spent on media:", percentage_per_day)