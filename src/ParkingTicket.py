import ParkingSlot


class ParkingTicket():
	def __init__(self, vehicle, slot):
		self.__vehicle = vehicle
		self.__alloted_slot = slot

	def get_slot(self):
		return self.__alloted_slot

