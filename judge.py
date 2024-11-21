#! /usr/bin/python3
from Crypto.Cipher import DES
from pwn import *
from random import randint

try:
    io = process("./main")
except:
    os.system("gcc main.c -o main")
    io = process("./main")

count = int(input("Enter the number of test runs: "))
for i in range(count):
    key = randint(0, 0xffffffffffffffff).to_bytes(8, "big")
    mytext = randint(0, 0xffffffffffffffff).to_bytes(8, "big")
    mode = str(randint(1, 2)).encode()
    cipher = DES.new(key, DES.MODE_ECB)
    if (mode == b"1"):
        res = cipher.encrypt(mytext).hex().encode()
    else:
        res = cipher.decrypt(mytext).hex().encode()
    io.sendline(mode)
    io.sendline(key.hex())
    io.sendline(mytext.hex())
    io.recvuntil(b"Result: ")
    
    ret = io.recvuntil(b"\n")[2:-1]
    if  ret != res:
        print(f"The {count}th test is failed!")
        print(f"mode={mode.decode()}\tkey={key.hex()}\ttext={mytext.hex()}")
        print(f"return  res={ret.decode()}\ncorrect res={res}")
        exit(1)
    else:
        if (mode == b"1"):
            mode = "encrypt"
        else:
            mode = "decrypt"
        print(f"The {i+1}th test is passed!\t Mode:"+mode)
print("Passed tests!")