from collections import Counter

numbers=[1,5,3,4,6,7,8,3,5,6,9,4,3,5,2]
c=Counter(numbers)
print(c.most_common(3))