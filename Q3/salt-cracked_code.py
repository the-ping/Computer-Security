import itertools
import hashlib
import collections

# 1. extract all salts to a file. 10K of them
file_read = open(r"rockyou-samples.sha1-salt.txt", "r") #open file to read n write
split = [entry.split("$") for entry in file_read]
salts = ([i[2] for i in split])

# 2. extract all hashes to another file.
file_read = open(r"rockyou-samples.sha1-salt.txt", "r") #open file to read n write
hashes = set([i[3].replace('\n', '') for i in split]) #set for faster access

# 3. store the 25 passwords in list
most_com_pass = (['123456', '12345', '123456789', 'password', 'iloveyou', 'princess', '1234567', 'rockyou', '12345678', 'abc123', 'nicole', 'daniel', 'babygirl', 'monkey', 'lovely', 'jessica', '654321', 'michael', 'ashley', 'qwerty', '111111', 'iloveu', '000000', 'michelle', 'tigger'])

# 4. concat salts to passwords. hash them
# saltedpasswords:passwords
saltedpass = {(a+b):b for a,b in itertools.product(salts, most_com_pass)} #combine salts to passwords
hashedsalt_pass = {(hashlib.sha1((s).encode())).hexdigest():p for (s,p) in saltedpass.items()}  #hash then store them
# print(len(hashedsalt_pass)) #2.5mil

# filter_hashedsalt_pass = {h:hashedsalt_pass[h] for h in hashedsalt_pass.keys() if h in hashes}
filter_hashedsalt_pass = {h:p for (h,p) in hashedsalt_pass.items() if h in hashes} # collect only hashes that exist is rockyou txt file

# 5. count no. occurences of each of the 25 passwords
c = collections.Counter(filter_hashedsalt_pass.values()) #dictionary of password:count

#main
#write every entry in c to file_writeto
file_writeto = open(r"salt-cracked.txt", "w") #open file to write
for (k,v) in c.items():
        file_writeto.write(str(v) + "," + k + "\n")

# ----------------------------------------------
#close file after opening it
file_writeto.close()
file_read.close()
#change access mode to allow read
file_writeto = open(r"salt-cracked.txt", "r+")
# print file_read.read()
print (file_writeto.read())
