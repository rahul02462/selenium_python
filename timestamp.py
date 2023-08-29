from datetime import datetime, timedelta

# Get the current date
current_date = datetime.now()

# Calculate the weekday of the current date (Monday is 0 and Sunday is 6)
weekday = current_date.weekday()

# Calculate the timedelta to go back to the last Saturday
days_to_last_saturday = (weekday - 6) % 7  # Subtracting 5 to move to Saturday
last_saturday = current_date - timedelta(days=days_to_last_saturday)

# Calculate the timedelta to go back to the last-to-last Sunday
days_to_last_to_last_sunday = (weekday - 6) % 7  # Subtracting 6 to move to Sunday
last_to_last_sunday = current_date - timedelta(days=days_to_last_to_last_sunday)

print("Last Saturday:", last_saturday.strftime("%Y-%m-%d"))
print("Last-to-last Sunday:", last_to_last_sunday.strftime("%Y-%m-%d"))
