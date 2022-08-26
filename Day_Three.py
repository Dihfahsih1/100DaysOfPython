#lamda function
multiply=lambda x, y: x * y

print(multiply(2,3))

'''python Global collections'''
number=[1,2,3, 4, 5,6 ,8, 9, 10]
# def double(a):
#   return a * 2 
# result = map(double, number)
# print(list(result))

# we can achieve the same using the lambda function
res=map(lambda a: a*2,number)
print(list(res))

res=filter(lambda a: a % 2 ==0 ,number)
print(list(res))