from string import ascii_lowercase
from itertools import product
import hashlib
from string import digits
import time
import collections
import itertools

file_read = open(r"rockyou-samples.md5.txt", "r+") #open file to read n write
file_writeto = open(r"md5-cracked.txt", "w") #open file to write

#-----------------------------------------------

#create a list of these: permutate through all possible 5char passwords
fivechar_list = [a+b+c+d+e for a,b,c,d,e in product(ascii_lowercase+digits, repeat=5)]

#hash all 5char words, give list of hashes
hash_list = [(hashlib.md5(i.encode())).hexdigest() for i in fivechar_list]

#map password to its hash
pass_hash = dict(itertools.izip(fivechar_list, hash_list)); #this might not allow repeats...

#store rockyou's file of hashes in list
file_read = open(r"rockyou-samples.md5.txt", "r") #open file to read n write
rockyou_list = [l.rstrip('\n') for l in file_read] #with repetitions

#Counter() rockyou_list, count how many times a hash in text file has occured
c1 = collections.Counter(rockyou_list) #a dictionary: [('e10adc3949ba59abbe56e057f20f883e', 892), ('25f9e794323b453885f5181f1b624d0b', 250), ('827ccb0eea8a706c4c34a16891f84e7b', 224)]

#map a password to its count (from c1's Counter result)
exist_passwords = {k:c1.get(pass_hash.get(k)) for k in set(pass_hash.keys()) if pass_hash.get(k) in c1}; #2503 of them.

#main
#write every entry in exist_passwords to file_writeto
for i in exist_passwords.items():
    file_writeto.write(str(i[1]) + "," + str(i[0]) + "\n")

# ----------------------------------------------
#close file after opening it
file_writeto.close()
file_read.close()
#change access mode to allow read
file_writeto = open(r"md5-cracked.txt", "r+")
# print file_read.read()
print (file_writeto.read())
