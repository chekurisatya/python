class Car:
    car_wheels = 4

    def __init__(self, make :str, model: str, year: int):
        self.make = make
        self._model = model
        self.__year = year

    @classmethod
    def from_string(cls, string):
        make, model,year = string.split(",")
        return Car(make,model,year)

    def start_engine(self) -> str:
        return f"Engine Started."

    #Getter Method
    def get_year(self):
        return self.__year

    #Setter Method
    def set_year(self,year: int) -> str:
        try:
            if not isinstance(year, int):
                raise TypeError("Year must be of Type Integer")
            self.__year = year
        except TypeError as e:
            print(f"Invalid Type for Year",{e})
            return "Failed to update Year. Refer to Error Message"
        else:
            print("Car Year has been updated")
            return "Car Year successfully updated"

    def get_info(self) -> str:
        return f"Car Make:{self.make}, Car Model:{self.model}, Car Year:{self.__year}"

    @staticmethod
    def is_motor_vehicle():
        return True

    @property
    def model(self):
        return self._model


class ElectricCar(Car):

    def __init__(self, make: str, model: str, year: int, battery_charge: int):
        super().__init__(make,model,year)
        self.battery_charge = battery_charge

    def start_engine(self) -> str:
        return "Silent Start"


C1 = Car("Hyundai", "Tuscon",2021)
C2 = Car("Lincoln","Nautilus",2024)

print(C1._Car__year)
# car_log.info(C1.start_engine())
# car_log.info(C2.start_engine())
C1.set_year(2025)
print(C1.get_year())
print(C1.is_motor_vehicle())
# C2.set_year(2025)
# print(C1.year)
# print(C2.year)
# #EC1 = ElectricCar("Ford", "Mustang", 2024, 95)
# car_log.info(C1._Car__get_info())
# car_log.info(C2._Car__get_info())
# #car_log.info(EC1.start_engine())
# car_log.info(f"{C1.make} {C1.model} has {C1.car_wheels} wheels")
# car_log.info(f"{C2.make} {C2.model} has {C2.car_wheels} wheels")
# #car_log.info(f"{EC1.make} {EC1.model} has {EC1.car_wheels} wheels")
C3 = Car.from_string("Tesla,Model S,2023")
print(C3.get_info())
print(C1.model, C2.model, C3.model)

