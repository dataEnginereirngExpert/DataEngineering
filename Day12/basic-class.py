class myclass:
    mynum=1234
    def say_hello(name):
        print(f"Hello {name}")
print(myclass.mynum)
myclass.mynum=5678
print(myclass.mynum)

myclass.say_hello("Amit")
