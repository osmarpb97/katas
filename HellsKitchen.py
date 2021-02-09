from re import sub
def gordon(a:str):
    up = a.upper().replace(' ', '!!!! ').replace('A','@') + '!!!!'
    return sub("E|I|O|U", "*", up)

print(gordon('are you stu pid'))