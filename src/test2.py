from Crypto.PublicKey import RSA

code = "nooneknows"
key = RSA.generate(2048)
encrypted_key = key.exportKey(passphrase=code, pkcs=8, protection="scryptAndAES128-CBC")
with open("privatersakey.bin", "wb") as f:
    f.write(encrypted_key)
with open("publickey.pem", "wb") as f:
    f.write(key.publickey().exportKey())

