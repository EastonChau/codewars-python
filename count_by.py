def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    r = 0
    array = [0] * n
    for i in range(n):
        array[i] = r + x
        r += x
    
    return array