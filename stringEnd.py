#Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

def solution(text, ending):
    endLen = len(ending)
    textLen = len(text)
    if endLen > textLen:
        return False
    elif text[-endLen : ] == ending:
        return True
    else:
        return False

