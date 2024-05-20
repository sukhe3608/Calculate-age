from datetime import datetime 
import time
from calendar import isleap

# Function to calculate age based on date of birth and present date
def calculate_age_data(dob, present_date):
    try:
        # Convert string dates to datetime objects
        dob = datetime.strptime(dob, '%Y-%m-%d')
        present_date = datetime.strptime(present_date, '%Y-%m-%d')
    except ValueError:
        # Handle incorrect date format
        print("Wrong format! please enter in (YYYY-MM-DD)")
        return None
    
    # Determine the age by comparing year, month, and day
    if (present_date.month, present_date.day) < (dob.month, dob.day):    
        age = present_date.year - dob.year - 1 
    elif (present_date.month, present_date.day) == (dob.month, dob.day):
        age = present_date.year - dob.year
    else:
        age = present_date.year - dob.year
    return age

# Function to check if a year is a leap year
def check_leap_year(year):
    return isleap(year)

# Function to return the number of days in a month, considering leap years
def month_days(month, leap_year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month == 2 and leap_year:
        return 29
    elif month == 2 and not leap_year:
        return 28
    elif month in [4, 6, 9, 11]:
        return 30

def main():
    # Get user input for name, date of birth, and present date
    name = input("Enter your name: ")
    dob = input("Enter the DATE OF BIRTH(YYYY-MM-DD): ")
    present_date = input("Enter the PRESENT DATE(YYYY-MM-DD): ")
    
    # Calculate age
    age = calculate_age_data(dob, present_date)
    if age is not None:
        print(f"{name} your age is: {age}")
    else:
        print("Age Calculation Failed!")
        return  # Exit the function if age calculation fails
    
    # Get the current local time
    local_time = time.localtime(time.time())
    
    # Calculate age in years and months
    year = int(age)
    month = year * 12 + local_time.tm_mon
    
    # Initialize day counter
    day = 0

    # Calculate the number of days lived by summing up days from each year
    begin_year = int(local_time.tm_year) - year
    end_year = begin_year + year

    for i in range(begin_year, end_year):
        if check_leap_year(i):
            day += 366
        else:
            day += 365

    # Add days from the current year until the current month
    leap_year = check_leap_year(local_time.tm_year)
    for m in range(1, local_time.tm_mon):
        day += month_days(m, leap_year)

    # Add days from the current month
    day += local_time.tm_mday

    # Print the age in years, months, and days
    print(f"{name}'s age is {year} years or {month} months or {day} days")

if __name__ == "__main__":
    main()
