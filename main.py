from lib import animator, animation_types, game_controller, builder
import simpleaudio as sa
import sys

def intro():
    wave_obj = sa.WaveObject.from_wave_file("assets/music.wav")
    play_obj = wave_obj.play()
    animator.animator().animate_singleline(animation_types.animationtypes.BANNER.value, 1.0, 1)
    animator.animator().animate_singleline(animation_types.animationtypes.PATH_BANNER.value, 1.0, 1)
    play_obj.stop()

def outro():
    pass

def game_loop(controller):
    try:
        u_input = input("pain >> ")
        r = controller.handle_input(u_input)
        if r[0] == 1:
            animator.animator().animate_multiline([animation_types.animationtypes.OUTRO_ONE.value, animation_types.animationtypes.OUTRO_TWO.value], 1.0, 8)
            sys.exit()
        else:
            game_loop(controller)
    except Exception as e:
        print(e)
        print("pain >> enter exit to close the game")
        game_loop(controller)


def main():
    intro()
    print("pain >> WELCOME TO PATH OF PAIN UNBELIEVING CREATOR \press 'h' for help" )
    game_loop(game_controller.gamecontroller(builder.map(256)))


main()


