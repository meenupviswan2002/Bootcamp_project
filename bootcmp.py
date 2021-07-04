import hashlib
str = raw_input("Enter a word:") 
str = str.encode(encoding="utf-8")
str = hashlib.md5(str)
print("Hash of the entered string is ")
print(str.hexdigest())

