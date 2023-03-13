#Public fields
#car is-a vehicle
class Vehicle:
    def __init__(self,engine_type,tyres):
        self.engine_type=engine_type
        self.tyres=tyres

    def print_details(self):
        print(f"Vehicle Info = {self.engine_type}  {self.tyres}")

class Car(Vehicle):
    def __init__(self,engine_type,tyres,model,company):
        Vehicle.__init__(self,engine_type,tyres)
        self.model=model
        self.company=company

    def print_details(self):
        Vehicle.print_details(self)
        print(f"Vehicle Info = {self.model}  {self.company}")


c=Car("Petrol",4,"Maruti1234","Maruti")
c.print_details()
c.model="Honda"
c.print_details()