from string import ascii_lowercase
from string import digits
import itertools
import time
import collections
import hashlib
###########
# t_end = time.time() + 15
# while time.time() < t_end:
###########
#list of possible 5char passwords
fivechar_list = [a+b+c+d+e for a,b,c,d,e in itertools.product(ascii_lowercase+digits, repeat=5)]
# dist_list = fivechar_list #60466176 words --<1min run
# ---------------------------

hash_list = [(hashlib.md5(i.encode())).hexdigest() for i in fivechar_list]

file_read = open(r"rockyou-samples.md5.txt", "r") #open file to read n write
rockyou_list = [l.rstrip('\n') for l in file_read] #with reps
# rockyou_set = set(rockyou_list) #no reps

pass_hash = dict(itertools.izip(fivechar_list, hash_list)); #this might not allow repeats...

#Counter() rockyou_list
c1 = collections.Counter(rockyou_list) #a dictionary: [('e10adc3949ba59abbe56e057f20f883e', 892), ('25f9e794323b453885f5181f1b624d0b', 250), ('827ccb0eea8a706c4c34a16891f84e7b', 224)]

exist_passwords = {k:c1.get(pass_hash.get(k)) for k in set(pass_hash.keys()) if pass_hash.get(k) in c1}; #2503 of them becos set the pass as keys. hence unique.
print(len(exist_passwords))



#list of hashes from above list of brute force generated passwords
# hash_list = [(hashlib.md5(i.encode())).hexdigest() for i in fivechar_list]
# print(len(hash_list)) #1:15 run 60mil

# ---------
# pass_hash = dict(itertools.izip(fivechar_list, hash_list)); #this might not allow repeats...
# print(len(pass_hash))

#----------
#1. store rockyou's file of hashes in list, vs a list with repetitions removed
# file_read = open(r"rockyou-samples.md5.txt", "r") #open file to read n write
# rockyou_list = [l.rstrip('\n') for l in file_read] #with reps
# rockyou_set = list(set(rockyou_list)) #no reps
# print(rockyou_set[0:3]) #['a37f1e1ec9eaecc147b0a4d41547d709', 'ccf75e117a9c11100516657a983527be', '4857fa98298117aa29d71a7fa660b930\n', '64f20a50f57fc24ae105b747e9385e53\n']
# print(len(rockyou_list)) #100k
# print(len(rockyou_set)) #82k

#2.
# hash_ind = dict(zip(rockyou_set, range(len(rockyou_set))))
#cannot: dict.items()[0], can: list(dict.items())[0]
# print(list(hash_ind.items())[0]) #('d92e8c0c1363d3635bd500dc21fcd790', 0)
# map hash (from rockyou_list) to password
# rhash_pass = {r:p for r in rockyou_list for p in list(pass_hash.keys()) if pass_hash.get(p)==r }
# print(len(rhash_pass))

# count no. of occurences in hash

#----------
# hashmap.keys() #e.g. ugyu10
# hashmap.values() #e.g. d92e8c0c1363d3635bd500dc21fcd790
# pass_hash = {k:h for k in hashmap.keys() for h in hashmap.values() if h in ind_hash}
# exist_passwords = {s:k for k in list(hashmap.keys()) for s in str(rockyou_list.count(hashmap.get(k)) if hashmap.get(k) in hash_ind}
# exist_passwords = {k:v for k in list(hashmap.keys()) for v in hashmap.get(k) if v in hash_ind};
# exist_passwords = {s:k for k in list(hashmap.keys()) if hashmap.get(k) in hash_ind for s in str(rockyou_list.count(hashmap.get(k)))};
# pass_hash = {p:h for (p, h) in hashmap.items() if h in hash_ind}
# exist_passwords = {str(rockyou_list.count(hashmap.get(k))):k for k in list(hashmap.keys()) if hashmap.get(k) in hash_ind}; #20 of them if run for 15s. 20 becos dictionary couldnt store the same keys more than once
# exist_passwords = {k:str(rockyou_list.count(hashmap.get(k))) for k in list(hashmap.keys()) if hashmap.get(k) in hash_ind}; #2503 of them becos set the pass as keys. hence unique.

# exist_passwords = {str(rockyou_list.count(hashmap.get(p))):p for (p,h) in pass_hash.items()}
# count_pass = {if v in rockyou_set}
# print(pass_hash)
# print(len(pass_hash))
# print(len(rockyou_list))
# print(len(rockyou_set))
# print(len(hash_ind))
# print(exist_passwords)
# print(len(exist_passwords))

#
# for i in exist_passwords.items():
#     print(i)
#{'2': 'carol', '1': 'benny', '5': 'nancy', '4': 'oscar', '3': 'yummy', '7': 'cheer', '6': 'chris', '8': 'billy', '0': 'happy', '9': 'lucky'}

# count_pass = {str(sum(k for k in exist_passwords)):k }
# [val = k for k in exist_passwords if val]
# count_pass = {sum(val)}
# print(len(count_pass))
# c = Counter(exist_passwords);
# print(c.most_common(3))

# k = list(hashmap.keys())[0]
# print(k)
# val = list(hashmap.values())[0:4]
# print(val)
# v = hashmap.get(k)
# print(v)
# print(type(v))
# print(v in hash_ind)
