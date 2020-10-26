def xor_encrypt(array, key):
    output = []
    for index, x in enumerate(array):
        output.append(x ^ key[index % len(key)])
    return output


myMessage = "Hello"
myKey = "abc"

myEncryptedMessage = xor_encrypt([ord(x) for x in myMessage], [ord(x) for x in myKey])
myEncryptedMessage2 = "".join([chr(x) for x in myEncryptedMessage])
print(myEncryptedMessage2)
myNewMessage = xor_encrypt([ord(x) for x in myEncryptedMessage2], [ord(x) for x in myKey])
myNewMessage2 = "".join([chr(x) for x in myNewMessage])
print(myNewMessage2)