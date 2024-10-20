
def encrypt_token(token, key):
    encrypted_token = ""
    for i, char in enumerate(token):
        decalage = ord(key[i % len(key)])
        code = (ord(char) + decalage) % 256
        encrypted_token += str(code) + " "
    return encrypted_token.strip()

token = input("token=")
key = input("key=")

print(encrypt_token(token,key))
