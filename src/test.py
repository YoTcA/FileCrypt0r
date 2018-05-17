import os, random, struct
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def encrypt():
    data = "Hello Wörld!".encode("utf-8")
    key = "1234567890123456".encode("utf-8")
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    file_out = open("encrypted2.bin", "wb")
    print(cipher.nonce)
    file_out.write(cipher.nonce)
    file_out.write(tag)
    file_out.write(ciphertext)


def decrypt():
    with open("encrypted2.bin", "rb") as file_in:
        key = "1234567890123456".encode("utf-8")
        #print(file_in.read(-1))
        nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]
        print(nonce)
        print(tag)
        print(ciphertext)
        cipher = AES.new(key, AES.MODE_EAX, nonce)
        data = cipher.decrypt_and_verify(ciphertext, tag)
        print("Data:" + data.decode("utf-8"))

encrypt()
decrypt()
