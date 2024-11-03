import calendar
import os

# Define the path and months
path = "/home/hxm/test/mds"
months = [
    "01_January",
    "02_February",
    "03_March",
    "04_April",
    "05_May",
    "06_June",
    "07_July",
    "08_August",
    "08_September",
    "10_October",
    "11_November",
    "12_December",
]

# Create the directory if it doesn't exist
os.makedirs(path, exist_ok=True)

# Get the year
year = 2024

for month_index, month in enumerate(months, start=1):
    # Create filename
    filename = f"{year}_{month}.md"
    file_path = os.path.join(path, filename)

    # Get the number of days in the month
    num_days = calendar.monthrange(year, month_index)[1]

    for day in range(1, num_days + 1):
        # Calculate the day of the year
        day_of_year = (
            sum(calendar.monthrange(year, m)[1] for m in range(1, month_index)) + day
        )

        # Get the weekday name
        weekday = calendar.weekday(year, month_index, day)
        day_name = calendar.day_name[weekday][:3]  # Get short day name (e.g., Mon, Tue)

        # Calculate week number
        week_number = (day_of_year - 1) // 7 + 1

        # Format the date string
        date_str = f"## {year}/{month_index:02}/{day:02} {day_name}. day{day_of_year:03} week{week_number:02}"

        # Write to the file
        with open(file_path, "a") as file:
            file.write(date_str + "\n\n\n")  # Followed by three blank lines

print("Markdown files generated successfully.")
