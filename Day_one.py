#Pythonic way of counting objects
word = "python"
counter = ()
for letter in word:
    if letter not in counter:
        counter[letter]=0
    counter[letter] +=1