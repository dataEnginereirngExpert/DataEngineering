def add (a,b):
 return  a+b

print(add(2,3))
print("-----------------")

add1= lambda a,b : a+b
print(add1(2,3))

# Square of a given number 

squared= lambda n: n**2
print(squared(3))

#maximum of given 2 values 
maximum=lambda x,y : x if x > y else y
print(maximum(8,7))


print("-----------------")

#map() function usage 
numbers=[1,2,3,4,5]
sqnumbers= list(map(lambda x:x**2,numbers))
sqnumbers1= list(map(squared,numbers))
print(sqnumbers)
print(sqnumbers1)

#filter() function usage 

numbers3=[10,15,20,25,30]
even_numbers= list(filter(lambda x: x%2==0,numbers3))
print(even_numbers)
