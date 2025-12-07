from animals import Animal
from dogs import Dog

# Creating object of Parent Class (Animal)
lion = Animal("Lion")

# Creating object of Child Class (Dog)
buddy = Dog("Buddy")

# Using Animal object
print(lion.eat())
print(lion.sound())

# Using Dog object
print(buddy.eat())       # inherited from Animal
print(buddy.sound())     # overridden in Dog
print(buddy.fetch())     # Dog-specific method
