def decrypt(encrypted_text, n):
    pass

def encrypt(text, n):
    if n:
        enc_text = [letter for letter in text]
        print(list(filter(lambda(i,x): text.index(e), enumerate(enc_text))))
    return text
        
    

print(encrypt("This is a test!", 1))