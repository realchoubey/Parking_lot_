from Vehicle import *


class ParkingSlot():
	def __init__(self, slot_number, vehicle_type=VehicleType.CAR):
		self.__slot_number = slot_number
		self.__vehicle = None
		self.__is_available = True


	def empty_slot(self):
		self.__vehicle = None
		self.__is_available = True


	def get_parked_vehicle(self):
		return self.__vehicle


	def park_vehicle(self, vehicle):
		self.__vehicle = vehicle
		self.__is_available = False


	def set_availablity(self, is_available):
		self.__is_available = is_available


	def is_available(self):
		return self.__is_available


	def get_slot_number(self):
		return self.__slot_number