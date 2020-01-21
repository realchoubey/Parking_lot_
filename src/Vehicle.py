from enum import Enum

# Enum for vehicle type, can use for extending 
# support for other type of vehicle.
class VehicleType(Enum):
	CAR, MOTORBIKE = 1, 2


# Base Vehicle class
class Vehicle():
	def __init__(self, v_number, v_color, v_type=VehicleType.CAR):
		self.__reg_number = v_number
		self.__type = v_type
		self.__color = v_color

	def get_reg_number(self):
		return self.__reg_number

	def get_vehicle_color(self):
		return self.__color


# Child Car class, it is inheriting Vehicle class.
class Car(Vehicle):
	def __init__(self, reg_number):
		super().__init__(reg_number, VehicleType.CAR)