#Protected Field
# CONVENTION

#car is-a vehicle
class Vehicle:
    def __init__(self,engine_type,tyres):
        self._engine_type=engine_type
        self._tyres=tyres

    def print_details(self):
        print(f"Vehicle Info = {self._engine_type}  {self._tyres}")

class Car(Vehicle):
    def __init__(self,engine_type,tyres,model,company):
        Vehicle.__init__(self,engine_type,tyres)
        self._model=model
        self._company=company

    def print_details(self):
        Vehicle.print_details(self)
        print(f"Vehicle Info = {self._model}  {self._company}")


c=Car("Petrol",4,"Maruti1234","Maruti")
c.print_details()
c._model="Honda" # Not recommended to change the fileds with one underscore
c.print_details()