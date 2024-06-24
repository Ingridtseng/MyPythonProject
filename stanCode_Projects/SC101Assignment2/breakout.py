"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics


FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    # Add the animation loop here!

    global NUM_LIVES
    counter = 0

    while NUM_LIVES > 0 and counter < graphics.numbricks:
        while True:
            graphics.ball_animation()
            vx = graphics.get_dx()
            vy = graphics.get_dy()
            if vx != 0:
                break
            pause(FRAME_RATE)

        while True:
            if counter >= graphics.numbricks:
                graphics.ball.x = graphics.window.width / 2 - graphics.get_ball_diameter() / 2
                graphics.ball.y = graphics.window.height / 2 - graphics.get_ball_diameter() / 2
                break

            if graphics.ball.x + graphics.get_ball_diameter() > graphics.window.width or graphics.ball.x <= 0:
                vx = -vx

            if graphics.ball.y <= 0:
                vy = -vy

            if graphics.ball.y + graphics.get_ball_diameter() > graphics.window.height:
                NUM_LIVES -= 1
                graphics.set_dx(0)
                graphics.set_dy(0)
                graphics.ball.x = graphics.window.width/2 - graphics.get_ball_diameter()/2
                graphics.ball.y = graphics.window.height/2 - graphics.get_ball_diameter()/2
                break

            maybe_object = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
            maybe_object_1 = graphics.window.get_object_at(graphics.ball.x+graphics.get_ball_diameter(), graphics.ball.y)
            maybe_object_2 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y+graphics.get_ball_diameter())
            maybe_object_3 = graphics.window.get_object_at(graphics.ball.x+graphics.get_ball_diameter(), graphics.ball.y+graphics.get_ball_diameter())

            if maybe_object is not None:
                if maybe_object == graphics.paddle:
                    if vy > 0:
                        vy = -vy
                else:
                    graphics.window.remove(maybe_object)
                    vy = -vy
                    counter += 1

            elif maybe_object_1 is not None:
                if maybe_object_1 == graphics.paddle:
                    if vy > 0:
                        vy = -vy
                else:
                    graphics.window.remove(maybe_object_1)
                    vy = -vy
                    counter += 1

            elif maybe_object_2 is not None:
                if maybe_object_2 == graphics.paddle:
                    if vy > 0:
                        vy = -vy
                else:
                    graphics.window.remove(maybe_object_2)
                    vy = -vy
                    counter += 1

            elif maybe_object_3 is not None:
                if maybe_object_3 == graphics.paddle:
                    if vy > 0:
                        vy = -vy
                else:
                    graphics.window.remove(maybe_object_3)
                    vy = -vy
                    counter += 1
            graphics.ball.move(vx, vy)
            pause(FRAME_RATE)


if __name__ == '__main__':
    main()
