#Comparision type, order of elements , contents , length 

namelist=['Amit','uttam']
print(namelist==['Amit'])
print(namelist==['Amit','uttam'])
print(namelist==['uttam','Amit'])
print(namelist==('Amit','uttam'))

#Containment testing  

name='Amit'
print('--------------------')
print('m' in name)
print('p' in name)
print(name in namelist)
print('ram' not in namelist)


#Concatination and repitition 

print('####################')
fname='amit'
lname='rastogi'
name1=fname+' '+lname
print(name1)
namelist2=namelist + ['shyam']
print(namelist2)

# repetitionn
name='ram'
repeatedname= (name+' ') * 3
print(name)
print(repeatedname)

#element extraction  index start from 0 and -index from length 
fullname="prashant kumar singh"   
print(fullname[3])
print(len(fullname))
print(fullname[-2])
print(fullname[0:8])
print(fullname[:])

message='i am in america'
print(message.index('e',3,14))


    



