f= open('D:\crfile.txt','r')
x=[]
f_contents=f.read()
x.append(f_contents)
print(x)
f.close()