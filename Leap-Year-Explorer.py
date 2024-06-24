def year_check(year):
    # Leap year condition: 
    # 1. If the year is divisible by 4 and not divisible by 100, or
    # 2. If the year is divisible by 400.
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True  #Leap year
    else:
        return False  #Not a leap year
 
year = input ("Please enter a year: ")

if year_check(int(year)):
    print("Leap Year")
else:
    print("Not a Leap Year")