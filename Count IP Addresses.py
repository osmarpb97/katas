def ips_between(start, end):
    s = list(map(int,start.split('.')))
    e = list(map(int,end.split('.')))
    return abs(sum([(s[i]-e[i])*pow(256,3-i) for i in range(4)]))
