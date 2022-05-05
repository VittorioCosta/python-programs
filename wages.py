name_ = str(input("name "))
wage_per_hour = float(input("wage per hour "))
hours = float(input("hours this week "))

extrahours = hours - 40
extrapay = (wage_per_hour + (wage_per_hour*0.5))

if hours <= 40: w = hours*wage_per_hour
elif hours > 40: w = (40*wage_per_hour) + (extrahours*extrapay)

print(w, "£")
