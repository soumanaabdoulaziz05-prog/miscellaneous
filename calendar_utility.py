import calendar
import datetime

# Get year and month from the user
year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))

# Display the calendar
print("\n--- Calendar ---")
print(calendar.month(year, month))

# Get today's date
today = datetime.date.today()

# Check if today is in the specified month and year
if today.year == year and today.month == month:
    print(f"Today is {calendar.month_name[month]} {today.day}, {today.year}")
else:
    print(
        f"Today is not in {calendar.month_name[month]} {year}."
    )

# Display today's date
print(f"Today's date: {today}")