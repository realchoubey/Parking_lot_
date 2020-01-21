import unittest
import Environment
import ParkingLot

class TestParkingLot(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parking_lot = ParkingLot.ParkingLot()
        cls.allocated_slot = 1

    def test_a_create_parking_lot(self):
        no_of_slots = 6
        self.parking_lot.create_parking_lot(no_of_slots)
        self.assertEqual(len(self.parking_lot.slots),
                         no_of_slots, msg="Error while creating parking lot.")

    def test_b_park(self):
        reg_number = "KA-01-HH-1234"
        color = "White"

        self.parking_lot.park(reg_number, color)
        self.assertFalse(self.parking_lot.slots[self.allocated_slot].is_available(),
                         "Parking failed.")

        for slot in self.parking_lot.slots.values():
            if not slot.is_available() and slot.get_parked_vehicle():
                self.assertEqual(slot.get_parked_vehicle().get_reg_number(),
                                 reg_number, "Parking failed")
                self.assertEqual(slot.get_parked_vehicle().get_vehicle_color(),
                                 color, "Parking failed")

    def test_c_leave(self):
        self.parking_lot.leave(self.allocated_slot)
        self.assertTrue(self.parking_lot.slots[self.allocated_slot].is_available(),
                        "Error while leaving parking lot.")

    @classmethod
    def tearDownClass(cls):
        del cls.parking_lot

if __name__ == '__main__':
    unittest.main()