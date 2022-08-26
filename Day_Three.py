#lamda function
multiply=lambda x, y: x * y

print(multiply(2,3))

'''python Global collections'''
number=[1,2,3]
# def double(a):
#   return a * 2 
# result = map(double, number)
# print(list(result))

# we can achieve the same using the lambda function
double = lambda a: a*2
res=map(double,number)
print(list(res))