import re
para = open("para.txt", "r")
reading = para.read()
print(reading)
paragraph = re.split(r'[\n]', reading)
lines = re.split(r'[.?]', reading)
words = re.split(r'[ \n,?.!]', reading)

print('Q1.Find the total number of paragraphs and total number of lines and words in each paragraph.\n')
print("The number of paragraph are", len(paragraph))
print("The number of lines are", len(lines))
print("The number of words are", len(words))


print('\n\nQ2.Find all the words that begin with vowel in the first paragraph & those which begin with consonants in the second paragraph\n')
print("*****************************************")
print("VOWELS")
print("*****************************************")
para1 = re.split(r'[ \n]', paragraph[0])
countvow = 0
for word in para1:
    if re.search(r'^[aeiouAEIOU]', word):
        countvow += 1
        print(word)
print("*****************************************")
print("CONSONANTS")
print("*****************************************")
countconst = 0
para2 = re.split(r'[ \n]', paragraph[2])
for word in para2:
    if re.search(r'^[^aeiouAEIOU]', word):
        countconst += 1
        print(word)

print('\n\nQ3.Find all the words having numerals\n')
countnum = 0
for w in range(len(words)):
    if re.search(r'[0-9]', words[w]):
        countnum += 1
        print(words[w])
print("\nWords having numerals are", countnum)

print("\n\nQ4.Find all the words which begin with letter 'data/Data/DATA'. If know such words exist then add such related words and repeat the search.\n")
countd = 0
words.append("This is my data ")
words.append("I am mining data ")
for i in range(len(words)):
    if re.search("data|Data|DATA", words[i]):
        countd += 1
        print(words[i])
print("\nWords which begin with letter 'data/Data/DATA' are", countd)

print("\n\nQ5.Find all the words which end with letter 'e'.\n")
countE = 0
for i in range(len(words)):
    if re.search(r'e$', words[i]):
        countE += 1
        print(words[i])
print("\nWords which end with letter 'e' are", countE)

print('\n\nQ6.Find all the words that begins with an vowel and ends with an vowel OR that begins with a consonant and ends with a consonant.\n')
countVowCon = 0
for w in range(len(words)):
    if re.search(r'^[aeiouAEIOU]', words[w]) and re.search(r'[aeiouAEIOU]$', words[w]) or re.search(r'^[^aeiouAEIOU]', words[w]) and re.search(r'[^aeiouAEIOU]$', words[w]):
        countVowCon += 1
        print(words[w])
print("\nWords that begins with an vowel and ends with an vowel OR that begins with a consonant and ends with a consonant are ", countVowCon)

print("\n\nQ7.Find all the words that have the letters 'to' in them, find the position of 'to' in each word.\n")
countTo = 0
for to in words:
    if re.search("to", to):
        countTo += 1
        print("The word : {} is in position : {}".format(to, to.index("to")))

print('\n\nQ8.Find all the words that have capital letters in them.\n')
countVowCon = 0
for w in range(len(words)):
    if re.search(r'[A-Z]+[a-z]+$', words[w]):
        countVowCon += 1
        print(words[w])

print('\n\nQ9.Find all the words that have special symbols in them\n')
countVowCon = 0
for w in range(len(words)):
    if re.search(r'(http://\S+|\S*[^\w\s]\S*)', words[w]):
        countVowCon += 1
        print(words[w])

print('\n\nQ10.Find the first occurence of fullstop in your input\n')
countVowCon = 0
for w in range(len(words)):
    if re.search(r'\.+', words[w]):
        countVowCon += 1
        print(words[w])

print('\n\nQ11.Find the words that dont have any vowel in them. If no such words exist add a few related words and repeat the task.\n')
countVowCon = 0
for w in range(len(words)):
    if re.search(r'[^aeiouAEIOU]+$', words[w]):
        countVowCon += 1
        print(words[w])

print("\n\nQ12.Find the first occurent of a word that does not begin with consonant but ends with 'ing' and has 'ta' in it.\n")
countVowCon = 0
for w in range(len(words)):
    if re.search(r'^[AEIOUaeiuo]+\w+ing$', words[w]):
        countVowCon += 1
        print(words[w])
    else:
        pass
