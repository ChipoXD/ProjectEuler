# ProblemURL: https://projecteuler.net/problem=59
# 65: A    90: Z
# 97: a    122: z
import string


def xor_encrypt_crack(array, allowed_char_array, allowed_char_key, key_length, key_words):
    output = []
    key_pointer = [0]*key_length
    for _ in range(len(allowed_char_key)**key_length):
        for key_index, key_element in enumerate(key_pointer):
            if key_element >= len(allowed_char_key):
                key_pointer[key_index] = 0
                key_pointer[key_index+1] += 1
        key = [allowed_char_key[x] for x in key_pointer]
        key_pointer[0] += 1
        decrypted_string = ""
        bad = False
        for array_index, array_element in enumerate(array):
            element = chr(array_element ^ ord(key[array_index % key_length]))
            if element not in allowed_char_array:
                bad = True
                break
            decrypted_string += element
        for key_word in key_words:
            if key_word not in decrypted_string:
                bad = True
                break
        if bad:
            continue
        output.append(decrypted_string)
    return output


ALLOWED_CHAR = string.ascii_letters + string.digits + string.punctuation + string.whitespace
f = open('Problem59data.txt', 'r')
encryptedMessage = [int(x) for x in f.read().strip().split(',')]
f.close()
suggestions = xor_encrypt_crack(encryptedMessage, ALLOWED_CHAR, string.ascii_lowercase, 3, [" the "])
decryptedMessage = suggestions[0]
sum = 0
for c in decryptedMessage:
    sum += ord(c)
print(sum)