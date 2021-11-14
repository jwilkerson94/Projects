# take input from the user and turn the word into pig latin version

def pigLatin(x):
    firstLetter = x[:1]
    removeFirstLetter = x[1:]
    addLatin = "-" + firstLetter + "ay"
    finalWord = removeFirstLetter + addLatin
    return finalWord

newVersion = pigLatin(input("Enter a word to be turned into pig latin: "))
print(newVersion)