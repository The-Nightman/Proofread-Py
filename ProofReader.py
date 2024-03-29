# Proofread script written by The-Nightman
# https://github.com/The-Nightman/Proofread-Py/

import string

word_dict = open("Proofreader\\words.txt")

proofread_input = input("Enter file path here:\n")

proofread_file = open(proofread_input)

file_extension = proofread_input.split(".")

while file_extension[-1] != "txt":
    proofread_file = input(
        ("unsupported file type, please enter path of txt file:"))
    file_extension = proofread_file.split(".")

file_read = proofread_file.read()

character_count = len(file_read)
space_count = file_read.count(" ")
underscore_count = file_read.count("_")
line_count = file_read.count("\n") + 1
word_count = len(file_read.split())
paragraph_count = file_read.count("\n\n") + 1

letter = 0
num = 0
for i in file_read:
    if i.isalpha():
        letter += 1
    elif i.isdigit():
        num += 1

specialchar_count = underscore_count + character_count - \
    (letter + num + space_count + (line_count - 1))

print(f"Characters (with spaces): {character_count}")
print(f"Characters (no spaces): {character_count - space_count}")
print(f"Spaces: {space_count}")
print(f"Digits: {num}")
print(f"Alphabetical characters: {letter}")
print(f"Special characters: {specialchar_count}")
print(f"Lines: {line_count}")
print(f"Words: {word_count}")
print(f"Paragraphs: {paragraph_count}")

spelling_reference = word_dict.read().casefold().translate(
    str.maketrans('', '', string.punctuation)).split()

user_spelling_input = file_read.casefold().translate(
    str.maketrans('', '', string.punctuation)).split()

for item in user_spelling_input[:]:
    if item in spelling_reference:
        user_spelling_input.remove(item)
    else:
        pass

print(f"please check for possible spelling mistakes:\n{user_spelling_input}")
