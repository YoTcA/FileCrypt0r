import os, random, struct
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data = "Hello World!".encode("utf-8")

key = "1234567890123456".encode("utf-8")
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)
file_out = open("encrypted.bin", "wb")
[ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]

# IV = 16 * '\x00'           # Initialization vector: discussed later
# mode = AES.MODE_CBC
# encryptor = AES.new(key, mode, IV=IV)
#
# text = 'j' * 64 + 'i' * 128
# ciphertext = encryptor.encrypt(text)
#
# print(ciphertext)

file_in = open("encrypted.bin", "rb")
nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]

# let's assume that the key is somehow available again
#cipher = AES.new(key, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(ciphertext, tag)
