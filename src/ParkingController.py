import os
import ParkingLot
import sys


class ParkingController(object):
    def __init__(self):
        self.parking_lot = ParkingLot.ParkingLot()


    def control_input_file(self, input_file):
        if not os.path.exists(input_file):
            print("Given file {} does not exist".format(input_file))

        file_obj = open(input_file)
        try:
            while True:
                line = file_obj.next()
                if line.endswith('\n'):
                    line = line[:-1]

                if line == '':
                    continue
                self.control_command(line)

        except StopIteration:
            file_obj.close()
        except Exception as e:
            print("Exception {} while processing input file.".format(e))


    def control_command_line(self):
        try:
            while True:
                interactive_input = raw_input("Enter command: ")
                self.control_command(interactive_input)
        except (KeyboardInterrupt, SystemExit):
            return
        except Exception as e:
            print("Exception {} while processing inputs.".format(e))


    def control_command(self, interactive_input):
        inputs = interactive_input.split()
        command = inputs[0]
        params = inputs[1:]
        if hasattr(self.parking_lot, command):
            command_function = getattr(self.parking_lot, command)
            command_function(*params)
        else:
            print("Please enter valid command. For details read README file.")


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 1:
        obj_parking_controller = ParkingController()
        obj_parking_controller.control_command_line()
    elif len(args) == 2:
        obj_parking_controller = ParkingController()
        obj_parking_controller.control_input_file(args[1])
