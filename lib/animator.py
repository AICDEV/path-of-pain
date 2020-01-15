from os import system
import sys
from lib import animations, animation_types
import time

class animator():
    def __init__(self):
        pass

    def animate_multiline(self, animation_names, time_offset, rounds):
        for anim in animation_names:
            if not self._validate_animation(anim):
                raise Exception("unsupported animation")
    
        for i in range(rounds):
            self._clear()
            if(len(animation_names) < 2):
                sys.stdout.writelines(self._load_animation(animation_names[0]))
     
            else:
                if i % 2 == 0:
                    sys.stdout.writelines(self._load_animation(animation_names[0]))
                else:
                    sys.stdout.writelines(self._load_animation(animation_names[1]))
            time.sleep(time_offset)
            self._clear()

    def animate_singleline(self, animation_name, time_offset, rounds):
        if not self._validate_animation(animation_name):
            raise Exception("unsupported animation")

        animation = self._load_animation(animation_name)
        for _ in range(rounds):
            for i in range(len(animation)):
                sys.stdout.writelines(animation[i])
                time.sleep(time_offset)
            self._clear()


    def _load_animation(self, name):
        return getattr(animations, name)

    def _validate_animation(self, name):
        return name in [item.value for item in animation_types.animationtypes]

    def _clear(self):
        system('clear')