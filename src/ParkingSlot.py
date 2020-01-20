import Vehicle

class ParkingSlot():
	def __init__(self, slot_number, vehicle_type=VehicleType.CAR):
		self.__vehicle = None
		self.__slot_number = slot_number
		self.__is_available = True

	def is_available(self):
		return self.__is_available

	def get_parked_vehicle(self):
		return self.__vehicle

	def park_vehicle(self, vehicle):
		self.__vehicle = vehicle

	def set_availablity(self, is_available):
		self.__is_available = is_available

	def get_availablity(self):
		return self.__is_available