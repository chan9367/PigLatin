import re

def pigLatin(word: str) -> str:
    # it returns the pig latin version of the input word
    vowels = 'aeiou'
    if word[0].lower() in vowels:
        ret = word+'way'
        return ret.lower()
    else:
        ret = word[1:]+word[0]+'ay'
        return ret.lower()

print("Enter a word to be pig latin: ")
word = input()
if re.match(r'\A[a-z-]+\Z', word.lower()):
    # check if the user input word is a valid word
    print(pigLatin(word))
else:
    print("Invalid word")