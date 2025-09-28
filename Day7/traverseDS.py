list2=[23,48,3,18,57,93]

# while loop - print 1-5 
a=5
while a < 5:
    a=a+1
    print('a value',a)

# 5,4,3,2,1 
b=5
while b>=1:
    print(b) #5, 4, 3, 2
    b=b-1
print('------------------------')
#for loop 
for i in range(10):
    print(i)
print('------------------------')
for i in range(1,10):
    print(i)

print('------------------------')
for i in range(1,10,2):
    print(i)


print('------------------------')
for i in range(15,5,-2):
    print(i)

print('------------------------')
for i in range(1,11):
    print(i)

# accessing list element using for loop
i=0
for listelement in list2:
    print(f'value at {i} is {listelement}')
    i=i+1