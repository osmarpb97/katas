
def rev(n):
    rev = 0;  
    while (n):  
        rem = n % 10;  
        rev = (rev * 10) + rem;  
        n = int(n / 10);  
    return rev;  

def is_pal(n):
    return n == rev(n)

def find_reverse_number(n):
    last = 0
    i=0
    while n:
        print(n)
        if is_pal(i):
            last = i
            n-=1
        i+=1
    return last

print(find_reverse_number(100))