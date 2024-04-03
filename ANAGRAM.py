# AUTHOR:- KUSH SHAH
def anagram(word1, word2):
    if sorted(word1) == sorted(word2):
        return True
    else:
        return False
    
if __name__ == "__main__":
    word1 = input("Enter first word: ")
    word2 = input("Enter second word: ")
    if anagram(word1, word2):
        print("Anagrams")
    else:
        print("Not anagrams")