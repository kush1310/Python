# AUTHOR:- KUSH SHAH
print("Enter date in format dd/mm/yyyy")
date = input("Enter date: ")
date = date.split("/")
print("Date in format mm-dd-yyyy: %s-%s-%s" % (date[1], date[0], date[2]))