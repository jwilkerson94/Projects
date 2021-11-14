# gets user input then counts the amount of vowels and displays that

def countVowels(x):
    aCount = x.count('a')
    eCount = x.count('e')
    iCount = x.count('i')
    oCount = x.count('o')
    uCount = x.count('u')
    
    fullCount = aCount + eCount + iCount + oCount + uCount
    print("The count of a is " + str(aCount) + "\nThe count of e is " + str(eCount) + "\nThe count of i is " + str(iCount) + 
    "\nThe count of o is " + str(oCount) + "\nThe count of u is " + str(uCount) + "\nThe full count is " + str(fullCount))


countVowels(input("Enter a word to see how many vowels are in it: "))