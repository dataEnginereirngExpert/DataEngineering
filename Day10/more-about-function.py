
def greetings(message , to='world'):
    return(message+ " "+to+"!")

print(greetings('hello'))
print(greetings('hello','India'))

def order_goods(customername,items):
    print(f" order received from {customername}")
    print(f" ordered items are {str(items)}")

# Calling funtion 
order_goods("amit",['sugar','tea'])

# make function capable to recevive  tuples as paramters 

def order_goods(customername,*items):
    print(f" order received from {customername}")
    print(f" ordered items are {str(items)}")

# Calling funtion 
order_goods("amit","atta","chawal","chini","chips")