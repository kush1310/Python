# AUTHOR:- KUSH SHAH
import string

def main ():

    # Get input file
    file = input("Please enter the name of the original file: ")
    infile = open(file, 'r')

    # get output file
    otherFile = input("Please enter the name of the file to write to: ")
    outfile = open(otherFile, 'w')

    # Change file
    for line in infile:
        words = line.split( )
        for word in words:
            counter = 0
            for letter in word:
                if not letter in string.punctuation:
                    counter += 1
            if counter == 4:
                if "." in word:
                    word = "****."
                elif "," in word:
                    word = "****,"
                elif "?" in word:
                    word = "****?"
                elif "!" in word:
                    word = "****!"
                else:
                    word = "****"
            

            print (word + " ", file = outfile, end = "")
        print("the data is printed in otherFile")
    # close files
    infile.close()
    outfile.close()

if __name__=='__main__':
    main ()