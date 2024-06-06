class car: 
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print('drive this car ')
class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("You are in the plane.")

class ship(): 
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("jump and swim ")
obj1 = car('kwid','renault')
obj2 = Plane('airindia','india')
obj3 = ship('cruise','goa')
            
for x in (obj1,obj2,obj3):
    x.move()

        