# AUTHOR:- KUSH SHAH
filename = input("Enter file name: ")
# open file in read mode
f = open(filename, "r")

# read the file
data = f.read()

# calculate average word length and sentence length

words = data.split()
sentences = data.split(".")
total_words = 0
total_sentences = 0

for word in words:
    total_words += len(word)
print("total characters are:",total_words)
for sentence in sentences:
    total_sentences += len(sentence)
print("total characters with space are:",total_sentences)
average_word_length = total_words / len(words)
average_sentence_length = total_sentences / len(sentences)

print(f"Average word length: {average_word_length}")
print(f"Average sentence length: {average_sentence_length}")