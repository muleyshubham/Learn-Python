#Private fields 
#car is-a vehicle
class Vehicle:
    def __init__(self,engine_type,tyres):
        self.__engine_type=engine_type
        self.__tyres=tyres

    def print_details(self):
        print(f"Vehicle Info = {self.__engine_type}  {self.__tyres}")

class Car(Vehicle):
    def __init__(self,engine_type,tyres,model,company):
        Vehicle.__init__(self,engine_type,tyres)
        self.__model=model
        self.__company=company

    def print_details(self):
        Vehicle.print_details(self)
        print(f"Vehicle Info = {self.__model}  {self.__company}")


c=Car("Petrol",4,"Maruti1234","Maruti")
c.print_details()
c.__model="Honda"
c.print_details()