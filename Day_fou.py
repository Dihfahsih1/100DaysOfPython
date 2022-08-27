#using reduce
from functools import reduce

expenses=[
          ('dick', 30),
          ('denis', 28)
          ]
sum = reduce(lambda n, m: n[1] + m[1],expenses) 

print(sum)