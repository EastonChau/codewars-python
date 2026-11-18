#For encrypting strings this region of chars is given (in this order!):
Region =  ([chr(i) for i in range(65, 91)] +  # all letters (ascending, first all UpperCase, 
    [chr(i) for i in range(97, 123)] + #then all LowerCase)
    [str(i) for i in range(0, 10)] +  #all digits (ascending)
    [i for i in '''.,:;-?! '()$%&"'''] #the following chars: .,:;-?! '()$%&"
)

#These are 77 chars! (This region is zero-based.)

'''
For building the encrypted string:

1. For every second char do a switch of the case.
2. For every char take the index from the region. Take the difference from the region-index of the char before (from the input text! Not from the fresh encrypted char before!). (Char2 = Char1-Char2)
3. Replace the original char by the char of the difference-value from the region. In this step the first letter of the text is unchanged.
Replace the first char by the mirror in the given region. ('A' -> '"', 'B' -> '&', ...)
'''

def encrypt(text):
    if not text:
        return text
    if any(c not in Region for c in text):
        raise Exception("Unknown characters")

    
    lastDigs1 = "".join(c.swapcase() if i%2 == 0 else c for i, c in enumerate(text[1:])) #1
    lastDigs2 = "".join(Region[Region.index(text[0]) - Region.index(c)] if i == 0 else Region[Region.index(lastDigs1[i - 1]) - Region.index(c)] for i, c in enumerate(lastDigs1)) #2
    firstDig = Region[76 - Region.index(text[0])] #3
    return firstDig + lastDigs2

def decrypt(encrypted_text):
    if not encrypted_text:
        return encrypted_text
    firstDig = Region[(76 - Region.index(encrypted_text[0]))] #3
    lastEncrypted_text = encrypted_text[1:]
    lastDigs = ""
    for i, c in enumerate(lastEncrypted_text):
        if i == 0:
            dif = Region.index(c) - 77 if Region.index(c) > Region.index(firstDig) else Region.index(c) #2
            thisDigIndex = Region.index(firstDig) - dif
            lastDigs += Region[thisDigIndex]
        else:
            dif = Region.index(c) - 77 if Region.index(c) > Region.index(lastDigs[-1]) else Region.index(c)
            thisDigIndex = Region.index(lastDigs[-1]) - dif
            lastDigs += Region[thisDigIndex]
    lastInput = "".join(c.swapcase() if i % 2 == 0 else c for i, c in enumerate(lastDigs)) #1
    return firstDig + lastInput