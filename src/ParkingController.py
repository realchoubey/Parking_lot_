import os
import ParkingLot
import sys


class ParkingController(object):
    """
    This class will be used as controller for parking lot.
    """
    def __init__(self):
        self.parking_lot = ParkingLot.ParkingLot()


    def control_input_file(self, input_file):
        """
        If file is provide we will parse it and read command.
        """
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
                self.__control_command(line)

        except StopIteration:
            file_obj.close()
        except Exception as e:
            print("Exception {} while processing input file.".format(e))


    def control_command_line(self):
        """
        Command line interface for user.
        """
        try:
            while True:
                interactive_input = raw_input("Enter command: ")
                self.__control_command(interactive_input)
        except (KeyboardInterrupt, SystemExit): # In case of exit called.
            return
        except Exception as e:
            print("Exception {} while processing inputs.".format(e))


    def __control_command(self, interactive_input):
        """
        Private function of class to run command.
        """
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
