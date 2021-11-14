# checks if the string is palindrome

def checkPalindrome(str):
    newStr = str[::-1]
    if(newStr == str):
        return True
    else:
        return False

inputWord = input("Enter a word to see if it is a palindrome: ")
result = checkPalindrome(inputWord)

if(result == True):
    print("The word (" + inputWord + ") is a palindrome.")
else:
    print("The word (" + inputWord + ") is not a palindrome.")
