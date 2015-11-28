myphrase = "the quick brown fox jumps over a lazy dog"
aphrase = "Python is a Global language"

def panagram(phrase):
    count=0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    phraseLetters=""
    for char in phrase:
        for letter in alphabet:
            if char == letter and char not in phraseLetters:
                phraseLetters += char
    
    for char in phraseLetters:
        for letter in alphabet:
            if char == letter:
                count+= 1
    if count == 26:
        print "The phrase is panagram"
    else:
        print "The phrase is not panagram"
        


panagram(myphrase)

                    



















        
