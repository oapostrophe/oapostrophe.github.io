import hashlib
string = "swow2015@mymail.pomona.edu"
string = string.encode()
result = hashlib.md5(string)
print(result)
print(result.hexdigest())
