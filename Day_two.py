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

#spliting
with open('example2.txt', "r") as reader:
  data=reader.readlines()
  for line in data:
    word = line.split()
    print(word)