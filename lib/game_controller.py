from lib import input_types, animator, animation_types
import sys

class gamecontroller():

    def __init__(self, map):
        self._map = map
        self._pos = map.get_start_position()
        self._animater = animator.animator()

    def handle_input(self, input):
        if not self._validate_user_input(input):
            print("pain >> sorry. unknown command. type h for more")
            return [0,0]
        if input == input_types.inputtypes.UP.value:
            return self._up()

        if input == input_types.inputtypes.DOWN.value:
            return self._down()

        if input == input_types.inputtypes.LEFT.value:
            return self._left()

        if input == input_types.inputtypes.RIGHT.value:
            return self._right()

        if input == input_types.inputtypes.INFO.value:
            self._info()
            return [0,0]

        if input == input_types.inputtypes.HELP.value:
            self._help()
            return [0,0]

        if input == input_types.inputtypes.EXIT.value:
            self._exit()

    def _up(self):
        return self._move([self._pos[0]+1,self._pos[1]])

    def _down(self):
        return self._move([self._pos[0]-1,self._pos[1]])

    def _left(self):
        return self._move([self._pos[0],self._pos[1]-1])

    def _right(self):
        return self._move([self._pos[0],self._pos[1]+1])

    def _move(self, pos):
        print(self._map.get_map()[pos[0]][pos[1]])
        if self._map.get_map()[pos[0]][pos[1]][5] == 0:
            self._animater.animate_multiline([animation_types.animationtypes.THE_WALL.value, animation_types.animationtypes.THE_WALL_TWO.value], 0.25, 4)
            return [0,0]

        if self._map.get_map()[pos[0]][pos[1]][8] == 1:
            return [1,0]

        self._pos = [pos[0],pos[1]]
        print(f"pain >> your new position is {self._pos}")
        return [0,1]

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
        print("pain >> h (help)")
        print("pain >> i (info)")
        print("pain >> exit")

    def _exit(self):
        raise SystemExit