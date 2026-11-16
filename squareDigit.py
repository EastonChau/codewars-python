#Square Every Digit

def square_digits(num):
    if num == 0:
        return 0
    number = int(num)
    length = len(str(num))
    numbers = [""] * length
    while number > 0:
        digit = number % 10
        numbers[length - 1] = str(digit ** 2)
        length -= 1
        number = number // 10

    return int(''.join(numbers))
