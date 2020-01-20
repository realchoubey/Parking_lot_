from enum import Enum
import ParkingTicket


class VehicleType(Enum):
	CAR, MOTORBIKE = 1, 2


class Vehicle():
	def __init__(self, v_number, v_color, v_type=VehicleType.CAR, ticket=None):
		self.__reg_number = v_number
		self.__type = v_type
		self.__color = v_color
		self.__ticket = ticket

	def assign_ticket(self, ticket):
		self.__ticket = ticket

	def get_assigned_ticket(self):
		return self.__ticket

	def get_reg_number(self):
		return self.__reg_number

	def get_vehicle_color(self):
		return self.__color


class Car(Vehicle):
  def __init__(self, reg_number, ticket=None):
    super().__init__(reg_number, VehicleType.CAR, ticket)