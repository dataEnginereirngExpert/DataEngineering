# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating."

    def sound(self):
        return f"{self.name} makes some sound."
