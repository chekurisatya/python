import logging

car_log = logging.getLogger("Car")
logging.basicConfig(level= logging.INFO)

class Car:
    """
    Car Class that will create a Car object for every unique car.
    """
    car_wheels = 4

    def __init__(self, make :str, model: str, year: int) -> object:
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self) -> str:
        """
        Class Method: start_engine

        Args: Class Object

        Returns:
            A print statement indicating that car engine has started
        """
        return f"Engine Started."

    def set_year(self,year: int) -> str:
        """
        Class Method: Car method, set_year, which will set the year of the car to input passed to the method.

        Args:
            a. Class Object
            b. Year: An integer only value
        Returns:
            Message saying that car year has been updated.
        Error:
            Type Error shall be raised if any type other than integer is encountered
        """
        try:
            if not isinstance(year, int):
                raise TypeError("Year must be of Type Integer")
            self.year = year
        except TypeError as e:
            car_log.error(f"Invalid Type for Year",{e})
            return "Failed to update Year. Refer to Error Message"
        else:
            car_log.info("Car Year has been updated")
            return "Car Year successfully updated"

    def get_info(self) -> str:
        """
        Class Method: Returns Details about the car

        Args:
            Class Object

        Return:
            Returns the Car attributes, Make, Model and Year
        """
        return f"Car Make:{self.make}, Car Model:{self.model}, Car Year:{self.year}"

class ElectricCar(Car):

    def __init__(self, make: str, model: str, year: int, battery_charge: int):
        super().__init__(make,model,year)
        self.battery_charge = battery_charge

    def start_engine(self) -> str:
        return "Silent Start"


C1 = Car("Hyundai", "Tuscon",2021)
C2 = Car("Lincoln","Nautilus",2024)

car_log.info(C1.start_engine())
car_log.info(C2.start_engine())
C1.set_year(2025)
C2.set_year(2025)
EC1 = ElectricCar("Ford", "Mustang", 2024, 95)

car_log.info(C1.get_info())
car_log.info(C2.get_info())
car_log.info(EC1.start_engine())
car_log.info(f"{C1.make} {C1.model} has {C1.car_wheels} wheels")
car_log.info(f"{C2.make} {C2.model} has {C2.car_wheels} wheels")
car_log.info(f"{EC1.make} {EC1.model} has {EC1.car_wheels} wheels")
