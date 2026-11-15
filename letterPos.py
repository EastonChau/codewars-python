#In this kata you are required to, given a string, replace every letter with its position in the alphabet.

#If anything in the text isn't a letter, ignore it and don't return it.

#"a" = 1, "b" = 2, etc.
def alphabet_position(text):
    code = ""
    positions = []
    lowercase = text.lower()
    
    letters = [chr(i) for i in range(97, 123)]
    for i in lowercase:
        if i in letters:   
            positions.append(letters.index(i)+1)
    
    strPositions = [str(p) for p in positions]
    code = ' '.join(strPositions)
    return code