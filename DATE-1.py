# AUTHOR:- KUSH SHAH
# Program to print the dates of all the Sundays in a given year.
def dates_of_sundays(year):
    import datetime
    for month in range(1, 13):
        for day in range(1, 32):
            try:
                date = datetime.date(year, month, day)
            except ValueError:
                continue
            if date.strftime("%A") == "Sunday":
                print(date.strftime("%d/%m/%Y"))
            
if __name__ == '__main__':
    year = int(input("Enter the year: "))
    dates_of_sundays(year)