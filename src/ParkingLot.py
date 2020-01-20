import ParkingSlot
import ParkingTicket
import Vehicle

class ParkingLot:
	instance = None

	class __SingleInstance:
	    def __init__(self, name):
	    	self.__name = name
	    	self.__slots = {}
	    	self.__vehicle_list = []
		    self.__active_tickets = {}
	
	def __init__(self, name, no_slot):
	   	if not ParkingLot.instance:
	   		ParkingLot.instance = ParkingLot.__SingleInstance(name)
	   	else:
	     	ParkingLot.instance.__name = name

	def __getattr__(self, name):
		return getattr(self.instance, name)
	
	def park_new_vehicle(self, vehicle):
		# Check if parking lot is full or have space:
		if not self.__is_full():
			ticket = ParkingTicket(vehicle)
			vehicle.assign_ticket(ticket)
			self.__active_tickets.put(1,1)
			self.__vehicle_list.append(vehicle)


	def create_parking_slots(self, no_of_slot):
		already_create_slots = self.__slots.size()

		for i in range(already_create_slots, no_of_slot + 1):
			self.__slots[i] = ParkingSlot(slot_number=i)


	def get_car_with_color(self, color):
		pass

	def get_slot_for_car(self, car_reg_num):
		pass

	def get_slot_with_color(self, color):
		pass


