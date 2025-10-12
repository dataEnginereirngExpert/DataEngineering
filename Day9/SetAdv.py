Set1={ 1,2,3} 
Set2={3,4,5}

Set3=Set1.union(Set2)
print(Set3)


Set4=Set1 | Set2
print(Set4)

Set5=Set1.intersection(Set2)
print(Set5)


Set6=Set1 & Set2
print(Set6)


Set7=Set1.difference(Set2)
print(Set7)
Set8=Set2-Set1
print(Set8)

#Containment test 
print(9 in  Set1)

SetA={1,2}
SetB={1,2,3,4,5}
print(SetA.issubset(SetB))
print(SetB.issuperset(SetA))


