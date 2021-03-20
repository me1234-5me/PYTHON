f = open("D:\crffile.txt", 'r')

f1 = open("D:\crfanswerfile.txt", 'w')

read = f.readline()
for i in range(0, len(read)):
    if i % 2 != 0:
        f1.write(read[i])

f1 = open("D:\crfanswerfile.txt", 'r')
c = f1.read()
print(c)
