def f():
 a=''
 for d in range(12):a+="On the %s day of Christmas\nMy true love sent to me\n%s\n"%("First|Second|Third|Fourth|Fifth|Sixth|Seventh|Eighth|Ninth|Tenth|Eleventh|Twelfth".split("|")[d],"\n".join("Twelve drummers drumm^,|Eleven pipers pip^,|Ten lords a-leap^,|Nine ladies danc^,|Eight maids a-milk^,|Seven swans a-swimm^,|Six geese a-lay^,|Five gold r^s,|Four call^ birds,|Three French hens,|Two turtle doves, and|A partridge in a pear tree.\n".replace('^','ing').split("|")[11-d:]))
 return a[:-2]

print(f())