#pip install english-words
from english_words import english_words_set

proofread_input = open(input("Enter file path here:\n"), "r")

file_read = proofread_input.read()

character_count = len(file_read)
space_count = file_read.count(" ")
underscore_count = file_read.count("_")
paragraph_count = file_read.count("\n\n")
word_count = len(file_read.split())

letter = 0
num = 0
for i in file_read:
    if i.isalpha():
        letter += 1
    elif i.isdigit():
        num += 1

line_count = 0
for line in open('Python\proofreadtest.txt'):
    line_count += 1

specialchar_count = underscore_count + character_count - (letter + num + space_count + (line_count - 1))

print(f"Characters (with spaces): {character_count}")
print(f"Characters (no spaces): {character_count - space_count}")
print(f"Spaces: {space_count}")
print(f"Digits: {num}")
print(f"Alphabetical characters: {letter}")
print(f"Special characters: {specialchar_count}")
print(f"Lines: {line_count}")
print(f"Words: {word_count}")
print(f"Paragraphs: {paragraph_count + 1}")