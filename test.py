f=open("test.txt","w")
f.write("my first file\n")
f.write("this file\n\n")
f.write("contains three lines\n")
f=open("test.txt",'r')
str=f.read()
print("read strings:",str)
f.close()
print(f.name,"is closed")
