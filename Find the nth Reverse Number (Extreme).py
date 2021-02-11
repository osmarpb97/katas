def find_reverse_number(n):
    n = n - 1                   # this kata assumes 1-based indices

    if n < 10:                  # tiny optimization
        return n

    x = n // 11                 # order of magnitude
    width = len(str(x))         # width of x
    nines = int("9"*width)      # the magic number
    lh = str(n - nines)         # the left side of the result
    rh = lh[:width][::-1]       # the right side of the result
    result = int(lh + rh)
    return result