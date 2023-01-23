sentence = input('Enter a sentence: ')

# split the sentence into a list of words
words = sentence.split()

# convert the first word to lowercase
words[0] = words[0].lower()

# loop through the rest of the words and capitalize the first letter
for i in range(1, len(words)):
    words[i] = words[i].capitalize()

# join the words together to form the camel case string
camel_case = ''.join(words)

print(camel_case)