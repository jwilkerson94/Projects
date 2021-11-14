# program to get user input and reverse it then output
 
def inReverse(x):
    return x[::-1]

toBeReversed = inReverse(input("Enter a string to get it reversed: "))
print("Your string but reversed:", toBeReversed)