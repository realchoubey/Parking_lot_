import ParkingSlot
import ParkingTicket
import Vehicle

class ParkingLot:
	instance = None

	class __SingleInstance:
	    def __init__(self, name="MyParkingLot"):
	    	self.__name = name
	    	self.__slots = {}
	    	self.__vehicle_list = []
	

	def __init__(self, name, no_slot):
	   	if not ParkingLot.instance:
	   		ParkingLot.instance = ParkingLot.__SingleInstance(name)
	   	else:
	     	ParkingLot.instance.__name = name


	def __getattr__(self, name):
		return getattr(self.instance, name)
	

	def create_parking_lot(self, no_of_slot):
		already_create_slots = self.__slots.size()

		for i in range(already_create_slots, no_of_slot + 1):
			self.__slots[i] = ParkingSlot(slot_number=i)


	def __get_next_available_slot(self):
		available_slots = filter(lambda slot: slot.is_available(), self.__slots.values())
		if not available_slots:
		    return None

		return sorted(available_slots, key=lambda slot: slot.get_slot_number())[0]


	def park(self, reg_number, color):
		self.park_new_vehicle(vehicle)


	def park_new_vehicle(self, vehicle):
		# Check if parking lot is full or have space:
		if not self.__is_full():
			slot = self.__get_next_available_slot()
			if slot:
				slot.park_vehicle(vehicle)
				slot.set_availablity(False)

			ticket = ParkingTicket(vehicle, slot)

			vehicle.assign_ticket(ticket)


			self.__vehicle_list.append(vehicle)


	def leave(self, slot_num):
		slot = self.__slots[slot_num]
		vehcile = slot.get_parked_vehicle()
		ticket_assigned = vehcile.get_assigned_ticket()

		slot_num = ticket_assigned.get_slot()
		slot.empty_slot()


	# Function to get list as per government regulation.
	def get_vehcile_with_color(self, color):
		list_vehicle_reg = []

		for vehicle in self.__vehicle_list:
			if vehicle.get_color() == color:
				list_vehicle_reg.append(vehicle.get_reg_number())

		return list_vehicle_reg


	def slot_number_for_registration_number(self, vehicle_reg_num):
		for slot_num, vehicle_d in self.__slots.items():
			if vehicle_d.get_reg_number() == vehicle_reg_num:
				return slot_num

		return -1


	def slot_numbers_for_cars_with_colour(self, color):
		list_slot_number = []
		for slot_num, vehicle_d in self.__slots.items():
			if vehicle_d.get_color() == color:
				list_slot_number.append(slot_num)

		return list_slot_number


