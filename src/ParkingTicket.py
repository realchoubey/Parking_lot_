import ParkingSlot


class ParkingTicket():
	"""
	Ticket will contain vehicle and parking slot information.
	This class can be extended to contain user details also.
	"""
	def __init__(self, vehicle, slot):
		self.__vehicle = vehicle
		self.__alloted_slot = slot

	def get_slot(self):
		return self.__alloted_slot
