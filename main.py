import hashlib
#pnf = password not found
pnf = True
def hashtxt(text):
    text_bytes = text.encode('utf-8')
    hash_object = hashlib.sha256(text_bytes)
    return hash_object.hexdigest()
while pnf:
    inp = input('Type your password: ')
    if hashtxt(inp) == "e0ecc78e7c4286e1f4556bc648c6d7ce5a60c9196c65ff02ae2c97d3f74811a7":
        pnf = False
    else:
        print('Try Agian')
print('Welcome')
