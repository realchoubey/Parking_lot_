import sys
import ParkingSlot
import ParkingTicket
from Vehicle import *


class ParkingLot:
	"""
	This is actual class for parking lot and it will be singleton.
	I will have all the functionality require to operate the parking lot.
	"""
	__instance = None

	class __SingleInstance:
	    def __init__(self, name):
	    	self.__name = name

	    	# Parking slot information.
	    	self.slots = {}

	    	# Currently parked vehicles
	    	self.vehicle_list = []
	

	def __init__(self, name="MyParkingLot"):
	   	if not ParkingLot.__instance:
	   		ParkingLot.__instance = ParkingLot.__SingleInstance(name)
	   	else:
	   		ParkingLot.__instance.__name = name


	def __getattr__(self, name):
		return getattr(self.__instance, name)
	

	def create_parking_lot(self, no_of_slot):
		"""
		Helper to create parking slots.
		"""
		try:
			for slot_number in range(1, int(no_of_slot) + 1):
				self.slots[slot_number] = ParkingSlot.ParkingSlot(slot_number=slot_number)

		except Exception as e:
			print("Exception {} occurred while initiating parking lot.".format(e))

		print("Created a parking lot with {} slots".format(no_of_slot))
		


	def __get_next_available_slot(self):
		available_slots = filter(lambda slot: slot.is_available(), self.slots.values())
		if not available_slots:
		    return None

		return sorted(available_slots, key=lambda slot: slot.get_slot_number())[0]


	def park(self, reg_number, color):
		obj_vehicle = Vehicle(v_number=reg_number, v_color=color)
		self.park_new_vehicle(obj_vehicle)


	def park_new_vehicle(self, vehicle):
		# Check if parking lot is full or have space.
		if self.__is_full():
			try:
				slot = self.__get_next_available_slot()
				if slot:
					slot.park_vehicle(vehicle)

				ticket = ParkingTicket.ParkingTicket(vehicle, slot)
				slot.assign_ticket(ticket)

				self.vehicle_list.append(vehicle)

				print("Allocated slot number: {}".format(slot.get_slot_number()))
			except Exception as e:
				print("Exception {} while parking vehicle".format(e))
		else:
			print("Sorry, parking lot is full.")



	def __is_full(self):
		# Instead of loop over to get nearest 
		# we can have heap to get nearest slot.
		for slot in self.slots.values():
			if slot.is_available():
				return True

		return False

	def leave(self, slot_num):
		"""
		Instead of directly emptying slot, I'm here getting the ticket 
		assigned to slot and then getting slot details because in real world 
		environment we will have to empty slot as per ticket received from 
		leaving user.
		"""
		try:
			slot = self.slots[int(slot_num)]
			if not slot.is_available():
				ticket_assigned = slot.get_assigned_ticket()
				slot = ticket_assigned.get_slot()
				self.vehicle_list.remove(slot.get_parked_vehicle())
				slot.empty_slot()
				print("Slot number {} is free".format(slot_num))
			else:
				print("No vehicle parked at slot {}.".format(slot_num))
		except Exception as e:
			print("Exception {} while leaving".format(e))


	def status(self):
		"""
		This print the status of parking lot as asked.
		"""
		print("Slot No. \t Registration No. \t Color")
		for slot in self.slots.values():
			if not slot.is_available():
				vehicle = slot.get_parked_vehicle()
				print("{} \t {} \t {}".format(slot.get_slot_number(),
					  vehicle.get_reg_number(), vehicle.get_vehicle_color()))


	def exit(self):
		sys.exit()


	# Function to get list as per government regulation.
	def registration_numbers_for_cars_with_colour(self, color):
		list_vehicle_reg = []

		try:
			for vehicle in self.vehicle_list:
				if vehicle.get_vehicle_color() == color:
					list_vehicle_reg.append(vehicle.get_reg_number())
		except Exception as e:
			print("Exception {} while getting cars with colors".format(e))

		print(list_vehicle_reg)


	def slot_number_for_registration_number(self, vehicle_reg_num):
		try:
			for slot in self.slots.values():
				if not slot.is_available():
					vehicle = slot.get_parked_vehicle()
					if vehicle.get_reg_number() == vehicle_reg_num:
						print(slot.get_slot_number())
						break
			else:
				print("Not found")
		except Exception as e:
			print("Exception {} while getting slots with registration number".format(e))


	def slot_numbers_for_cars_with_colour(self, color):
		list_slot_number = []
		try:
			for slot in self.slots.values():
				if not slot.is_available():
					vehicle = slot.get_parked_vehicle()
					if vehicle.get_vehicle_color() == color:
						list_slot_number.append(slot.get_slot_number())
		except Exception as e:
			print("Exception {} while getting slots with colors".format(e))

		print(list_slot_number)


