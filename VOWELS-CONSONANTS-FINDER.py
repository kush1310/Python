# AUTHOR:- KUSH SHAH
def count_vowels_consonants(s):
    vowels = "aeiou"
    count_vowels = 0
    count_consonants = 0
    for char in s.lower():
        if char in vowels:
            count_vowels += 1
        elif char.isalpha():
            count_consonants += 1
    return (count_vowels, count_consonants)

if __name__ == "__main__":
    s = input("Enter a string: ")
    count_vowels, count_consonants = count_vowels_consonants(s)
    print("Vowels: %d Consonants: %d" % (count_vowels, count_consonants))

#2nd method
# Program to count vowels, consonant, digits and special character in a given string. 
 
def countCharacterType(str): 
    vowels = 0
    consonant = 0
    specialChar = 0
    digit = 0

    for i in range(0, len(str)):  
        ch = str[i]  
        if ( (ch >= 'a' and ch <= 'z') or 
             (ch >= 'A' and ch <= 'Z') ):  
  
            ch = ch.lower() 
            if (ch == 'a' or ch == 'e' or ch == 'i' 
                        or ch == 'o' or ch == 'u'): 
                vowels += 1
            else: 
                consonant += 1
          
        elif (ch >= '0' and ch <= '9'): 
            digit += 1
        else: 
            specialChar += 1
      
    print("Vowels:", vowels) 
    print("Consonant:", consonant)  
    print("Digit:", digit)  
    print("Special Character:", specialChar)  
  
str = "KUSH SHAH"
countCharacterType(str)  