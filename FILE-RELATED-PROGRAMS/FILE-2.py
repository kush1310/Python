# AUTHOR:- KUSH SHAH
# Program to get letter count in a text file
def letterFrequency(fileName, letter):
    # open file in read mode
    file = open('data_file.txt', 'r')
 
    # store content of the file in a variable
    text = file.read()
 
    # using count()
    return text.count(letter)
print(letterFrequency('data_file.txt', 'o'))