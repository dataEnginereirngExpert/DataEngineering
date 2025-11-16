import mymodule

print(mymodule.add(2,3))
print(mymodule.greet("Amit"))

from mymodule  import calculator
calc=calculator() 
print(calc.multiply(2,3))