#Pythonic way of counting objectsz
word = "DIHFAHSIH"
counter = {}
for letter in word:
    if letter not in counter:
        counter[letter]=0
    counter[letter] +=1
print(counter)

#another way of counting objects using get()
word = ['Mathew','Mark', 'John','Mathew','Luke', 'Mathew', 'John']
counter = {}
for letter in word:
    counter[letter]=counter.get(letter, 0) +1 #we are getting the curent count of a given letter or 0 by default if the letter is missing, then we increment the count by 1 and store it under the corresponding letter in the dectionary
print(counter)