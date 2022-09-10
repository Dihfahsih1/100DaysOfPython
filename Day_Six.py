from collections import Counter
from statistics import mode

numbers=[1,5,3,4,6,7,8,3,5,6,9,4,4,5,2]
c=Counter(numbers)
print(c.most_common(3))

#mode returns the first most commonest in the list
#print(mode(numbers))