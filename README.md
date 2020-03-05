# cs-cw2-Computer-Security
topics: Asymmetric encryption with GPG, Spoofing email sender, Password cracking, Man in the middle attack

Q1.2 Encrypted email exercise
files:
- "fingerprint": uploaded to kerserver ('hkp://keys.gnup.net') the hexadecimal ID associated with my newly generated public key (Q1.2.2)
- "challenge_de": the secret message received via email, which was encrypted using my public key by my submitted fingerprint (from 1.2.2) 
- "solution": the revealed answer from "challenge_de". but encrypted using the public key from 1.2.4

Q3.1 Brute-forcing MD5
files:
- "brute_force_md5.py": code to encrypt then print passwords of the MD5 hashes from "rockyou-sample.md5.txt"
- "md5-cracked.txt": identified all existing 5-character passwords from "rockyou-sample.md5.txt"'s hashes

Q3.2 Cracking Common Passwords with Salted SHA-1
files:
- "salt-cracked_code.py": code to calculate how often a password occured in the "rockyou-samples.sha1-salt.txt" file
- "salt-cracked.txt": the results

Q3.3 Cracking bcrypt?
files:
- "bcrypt_cracking.py": code to get first five occurences of '123456'
- "bcrypt-lines.txt": printed line numbers where in the file '123456' is found 

Q4
files:
- "eve.py": code that implemented the Man-in-the-middle attack. 'eve' is the 'man-in-the-middle', intervening alice and bob's conversation
