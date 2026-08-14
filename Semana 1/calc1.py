name = input("Please enter your name:")
social_media = float(input("How many hours do you spend on social media?"))
whatsaap = float(input("How many hours do you spend on whatsaap?:"))
streaming_services = float(input("How many hours do you spend on streaming services?:"))
fortnite = float(input("How many hours do you spend on fortnite?:"))
others = float(input("How many hours do you spend on other media?:"))
total_hours = social_media + whatsaap + streaming_services + fortnite + others
percentage_per_day = (total_hours / 24) * 100
print("Username:", name)
print("Total hours spent on media:", total_hours)
print("Percentage of day spent on media:", percentage_per_day)