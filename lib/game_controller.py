from lib import input_types
import sys

class gamecontroller():

    def __init__(self, map):
        self._map = map 

    def handle_input(self, input):
        if not self._validate_user_input(input):
            print("pain >> sorry. unknown command. enter help")


        if input == "info":
            self._info()

        if input == "help":
            self._help()

        if input == "exit":
            self._exit()

    def _validate_user_input(self, input):
        return input in [item.value for item in input_types.inputtypes]

    def _info(self):
        print(f"pain >> your start is at: {self._map.get_start_position()}")
        print(f"pain >> your finish is at: {self._map.get_end_postion()}")

    def _help(self):
        print("pain >> the following commands are available \n")
        print("pain >> a (move left)")
        print("pain >> w (move up)")
        print("pain >> s (move down)")
        print("pain >> d (move right)")
        print("pain >> help")
        print("pain >> info")
        print("pain >> exit")

    def _exit(self):
        raise SystemExit