#String literals
myName='Uttam Kumar'
  
#String function 
#len function 
print(len(myName))
#splt()
print(myName.split())
myName1='UttamKumar@Deoghar'
print(myName1.split('@'))
#join()
fruits=['mango','apple','papaya']
newFruits=',,'.join(fruits)
print(newFruits)
newFruits1='-banana-'.join(fruits)
print(newFruits1)
#replace
sms='i am going to market'
print(sms)
print(sms.replace('market','office'))
#strip , to reomve white leading and trailing spaces from any string 

newnaem=' Amit Rastogi '
print(len(newnaem))
newnaem1=newnaem.strip()
print(len(newnaem1))
#lstrip and rstrip  

#String formatting : it is used to substitute the value in any string 
name="Amit"
age=25
info='Welcome {},you are {} years old'
print(info.format(age,name))

name1="AmitRastogi"
age1=25
info1=f"Welcoem {name1}, you are {age1} years old"
print(info1)
