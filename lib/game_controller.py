from lib import input_types
import sys

class gamecontroller():

    def __init__(self, map):
        self._map = map 
        self._pos = map.get_start_position()

    def handle_input(self, input):
        if not self._validate_user_input(input):
            print("pain >> sorry. unknown command. type help for more")

        if input == input_types.inputtypes.UP.value:
            self._up()

        if input == input_types.inputtypes.DOWN.value:
            self._down()

        if input == input_types.inputtypes.LEFT.value:
            self._left()

        if input == input_types.inputtypes.RIGHT.value:
            self._right()

        if input == input_types.inputtypes.INFO.value:
            self._info()

        if input == input_types.inputtypes.HELP.value:
            self._help()

        if input == input_types.inputtypes.EXIT.value:
            self._exit()


    def _up(self):
        pass

    def _down(self):
        pass

    def _left(self):
        pass

    def _right(self):
        pass

    def _validate_user_input(self, input):
        return input in [item.value for item in input_types.inputtypes]

    def _info(self):
        print(f"pain >> your start position is at: {self._map.get_start_position()}")
        print(f"pain >> your current position is at: {self._pos}")
        print(f"pain >> your finish position is at: {self._map.get_end_postion()}")

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