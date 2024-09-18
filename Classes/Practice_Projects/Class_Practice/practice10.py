'''
Multiple Inheritance
Write two base classes: ElectronicDevice with attribute brand and PortableDevice with attribute battery_life.
Create a derived class Smartphone that inherits from both and has an additional attribute camera_quality.
Add a method device_info that prints all attributes.
'''
class ElectronicDevice:
    # Base class with brand attribute
    def __init__(self, brand):
        self.brand = brand

class PortableDevice:
    # Base class with battery_life attribute
    def __init__(self, battery_life):
        self.battery_life = battery_life

class Smartphone(ElectronicDevice, PortableDevice):
    # Derived class with camera_quality attribute and device_info method
    def __init__(self,brand, battery_life, camera_quality, device_info):
        ElectronicDevice.__init__(self, brand)
        PortableDevice.__init__(self, battery_life)
        self.camera_quality = camera_quality
        self.device_info = device_info

    def smartPhone_info(self):
        return f"Phone Brand: {self.brand}, Battery Life: {self.battery_life}, Camera Quality: {self.camera_quality}, Device Info: {self.device_info}"

SMRTPH_1 = Smartphone("Samsung", "Good", "Excellent", "Non Professional Work Only.")
print(SMRTPH_1.smartPhone_info())