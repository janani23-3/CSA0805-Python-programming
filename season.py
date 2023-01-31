month = input("Input the month (e.g. January, February etc.): ")
day = int(input("Input the day: "))

if month in ('January', 'February', 'March'):
	season = 'winter'
elif month in ('April', 'May', 'June'):
	season = 'spring'
elif month in ('July', 'August', 'September'):
	season = 'summer'
else:
	season = 'autumn'

if (month == 'March') and (day > 20):
	season = 'summer'
elif (month == 'June') and (day > 21):
	season = 'spring'
elif (month == 'September') and (day > 22):
	season = 'fall'
elif (month == 'December') and (day > 21):
	season = 'winter'

print("Season is",season)
