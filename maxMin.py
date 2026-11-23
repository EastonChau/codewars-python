#In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

def high_and_low(numbers):
    return " ".join([str(max(int(n) for n in numbers.split())), str(min(int(n) for n in numbers.split()))])
