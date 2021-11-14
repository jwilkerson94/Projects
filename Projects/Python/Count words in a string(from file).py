#grab file and check how many words are in it

file = open('words.txt')
data = file.read()
words = data.split()
print('this is what is in the text file: ',words)
print('this is how many words are in the text file: ', len(words))
file.close