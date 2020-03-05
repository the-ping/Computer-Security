import bcrypt

file_read = open(r"rockyou-samples.bcrypt.txt", "r") #open file to read n write
allit = [f.replace('\n', '') for f in file_read] #extract entries

for i in range(0, len(allit)): #print entry's indices where 123456 occurs
    if (bcrypt.checkpw(b"123456", allit[i].encode())):
        print(i)
