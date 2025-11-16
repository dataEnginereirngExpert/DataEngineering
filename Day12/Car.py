class car:
    def __init__(self,name,brand):   #constrcutor , modelname and brandname are instance variable
        self.modelname=name
        self.brandname=brand

    def launch(self):
        print(f"{self.modelname} by {self.brandname} has been launched ! ")

mycar1=car("Fabia","skoda") #object creation 
#instance variable access 
print(mycar1.brandname)
print(mycar1.modelname)
mycar1.launch()

mycar2=car("Hector","MG") #object creation 
#instance variable access 
print(mycar2.brandname)
print(mycar2.modelname)
mycar2.launch()
    