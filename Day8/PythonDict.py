student_dict={100:'Amit',100:'uttam'}
#print(student_dict)

# to convert list into dictionary 
myList=[(101,'AMIT'),(102,'UTTAM')]
s_dict=dict(myList)
print(s_dict)
print(s_dict[102])
print(s_dict.keys())
print(s_dict.values())
print(s_dict.items())
del(student_dict)
print(student_dict)
