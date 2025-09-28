myset={1,2,3,4,5}
print(myset)
myset1={1,1,2,3,3,4,5,5}
print(myset1)

namelist=['Ram','shyam','Ram']
print(namelist)
newname=set(namelist)
print(newname)

newname1=list(newname)
print(newname1)

newname.add('hanuman')  # set function

print(newname)

newname.update(['jamband','sugriv'])
print(newname)

newname.remove('sugriv')
print(newname)