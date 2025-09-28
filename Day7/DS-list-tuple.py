list1=[1,2,3]
tuple1=(1,2,3)
list1[0]=7
print(list1)
print(type(list1))
#tuple1[0]=7    # this line will give erros as tuple is not updateable 
print(tuple1)
list1[0]="amit"
print(list1)
print(type(list1))

# predefined function test
list2=[23,48,3, 18]
tuple2=(25,2,53,9)

print('list2 value=>',len(list2),'tuple2 value=>',len(tuple2))
print('list2 min value=>',min(list2),'tuple2 min value=>',min(tuple2))
print('list2 max value=>',max(list2),'tuple2 max value=>',max(tuple2))

# list2.pop()
print('list2 value=>',list2)
list2.insert(0,99)
print('list2 value=>',list2)
