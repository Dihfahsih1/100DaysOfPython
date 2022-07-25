#Day Two
#File Handling
file=open('example1.txt', 'r')
f=file.read()
print(f)

#creating a file using write()
file=open('example2.txt','w')
file.write("This the first line")
file.write("\n")
file.write("This is the second line")
file.close()