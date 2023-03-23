import os
from cryptography.fernet import Fernet

mode = input("Do you want to receive or seand a message(r/s)?\n")



if mode == "s":
    file_s = input("Write message to be encrypted:\n")
    with open("file_s.txt", "w") as thefile:
        thefile.write(file_s)

    key = input("Enter the key for encryption: ")

    files = []
    for file in os.listdir():
        if file == "Enigma.py":
            continue
        files.append(file)

    for file in files:
        with open(file, "r") as thefile_s:
            contents_s = thefile_s.read()
        thefile_s_encrypted = Fernet(key).encrypt(contents_s)
        with open(file, "w") as thefile_s:
            thefile_s.write(thefile_s_encrypted)
else:
    file_r = input("Paste the message to decode here:\n")
    with open("file_r.txt", "w") as thefile_r:
        thefile_r.write(file_r)
    
    key_r = input("Input the key for decryption: ")
    
    files = []
    for file in os.listdir():
        if file == "Enigma.py":
            continue
        files.append(file)
    
    for file in files:
        with open(file, "r") as thefile_r:
            contents_r = thefile_r.read()
        contents_r_decrypted = Fernet(key_r).decrypt(contents_r)
        with open(file, "w") as thefile_r:
            thefile_r.write(contents_r_decrypted)