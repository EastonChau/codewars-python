def solution(number):
    n = int(number)
    if n <= 0:
        return 0
    else:
        multiples = []

        for i in range(n):
            if i == 0:
                continue
            
            if (i % 3 == 0) or (i % 5 == 0):
                multiples.append(i)
                
        return sum(multiples)
