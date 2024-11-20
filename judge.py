from Crypto.Cipher import DES

key = bytes.fromhex("3132333435363738")
ciphertext = bytes.fromhex("05cd4e9311ed3aae") 

cipher = DES.new(key, DES.MODE_ECB)

decrypted = cipher.encrypt(ciphertext)

print(decrypted.hex())
