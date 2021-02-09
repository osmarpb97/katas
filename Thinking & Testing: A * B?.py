def test_it(a, b):
    a_r = sum([int(element) for element in str(a)])
    b_r = sum([int(element) for element in str(b)])
    return a_r*b_r

print(test_it(12, 34))