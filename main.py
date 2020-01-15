from lib import animator, animation_types, game_controller, builder
import simpleaudio as sa
import sys

#animator.animator().animate([animation_types.animationtypes.TRAP.value, animation_types.animationtypes.TRAP_UP.value], 0.5, 8)

#animator.animator().animate_multiline([animation_types.animationtypes.TRAP.value, animation_types.animationtypes.TRAP_UP.value], 0.5, 8)



def intro():
    wave_obj = sa.WaveObject.from_wave_file("assets/music.wav")
    play_obj = wave_obj.play()
    animator.animator().animate_singleline(animation_types.animationtypes.BANNER.value, 1.0, 1)
    animator.animator().animate_singleline(animation_types.animationtypes.PATH_BANNER.value, 1.0, 1)
    play_obj.stop()

def game_loop(controller):
    try:
        u_input = input("pain >> ")
        controller.handle_input(u_input)

        game_loop(controller)
    except Exception as e:
        print(e)
        print("pain >> enter exit to close the game")
        game_loop(controller)


def main():
    # intro()
    game_loop(game_controller.gamecontroller(builder.map(256)))


main()