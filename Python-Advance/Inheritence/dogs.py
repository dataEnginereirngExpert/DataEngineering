from animals import Animal


# Child Class
class Dog(Animal):   # Dog inherits from Animal
    def sound(self):  # Overriding parent method
        return f"{self.name} barks."

    def fetch(self):
        return f"{self.name} is fetching the ball."