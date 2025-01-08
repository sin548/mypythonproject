"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

Added a scoreboard on top of the original setup, where the speed increases every 10 points.
Also added two buffs: when a brick disappears, two rectangles are randomly generated,
which will either increase or decrease the paddle's length.
"""

from campy.gui.events.timer import pause
from brackoutgraphics import BreakoutGraphics
from campy.graphics.gobjects import GRect

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    graphics.score = 0
    vx = 0
    vy = 0
    buff_vy = graphics.get_vy()//1.5
    ball = graphics.ball
    paddle = graphics.paddle
    window = graphics.window
    buffs = []
    # Add the animation loop here!
    while True:
        if graphics.pause_switch:
            pause(FRAME_RATE)

        #  Interpretation of the object before the ball falls below the window.
        elif ball.y < window.height:
            if vx == 0 and vy == 0:
                vx = graphics.get_vx()
                vy = graphics.get_vy()
            ball.move(vx, vy)

            # The ball bounces back when it hits the left or right side of the window.
            if ball.x < 0 or ball.x + ball.width > window.width:
                vx = -vx
            # The ball bounces back when it hits the top of the window.
            if ball.y < 0:
                vy = -vy

            # check if hit paddle or bricks
            top_left = window.get_object_at(ball.x, ball.y)
            top_right = window.get_object_at(ball.x + ball.width, ball.y)
            bottom_left = window.get_object_at(ball.x, ball.y + ball.height)
            bottom_right = window.get_object_at(ball.x + ball.width, ball.y + ball.height)
            for obj in [top_left, top_right, bottom_left, bottom_right]:
                if obj is not None and obj is not graphics.scoreboard:
                    if obj is paddle:
                        # Prevent the ball from bouncing up and down when colliding with the sides of the paddle.
                        if vy > 0:
                            vy = -vy
                        ball.y = paddle.y - ball.height
                        break
                    elif obj in buffs:
                        pass
                    else:
                        window.remove(obj)
                        graphics.score += 1
                        graphics.scoreboard.text = "Score: "+str(graphics.score)
                        vy = -vy
                        buff = graphics.random_buff()
                        if buff:
                            buffs.append(buff)
                            window.add(buff, x=ball.x, y=ball.y)
                        if graphics.score % 10 == 0:  # Increase speed per 10 points
                            vx += 1
                            vy += 1
                        break

            for buff in buffs:
                buff.move(0, buff_vy)
                # Treat buffs' collisions and their effects.
                if check_collision(buff, paddle):  # can not use rect1
                    buffs.remove(buff)
                    window.remove(buff)
                    if buff is graphics.rect1:
                        if paddle.width < window.width:
                            new_width = paddle.width + 20
                            window.remove(paddle)
                            paddle = GRect(new_width, graphics.paddle_height, x=paddle.x, y=paddle.y)
                            paddle.filled = True
                            window.add(paddle)
                            graphics.paddle = paddle  # Rebind the new paddle to the onmousemove event.
                    if buff is graphics.rect2:
                        if paddle.width > ball.width:
                            new_width = paddle.width - 20
                            window.remove(paddle)
                            paddle = GRect(new_width, graphics.paddle_height, x=paddle.x, y=paddle.y)
                            paddle.filled = True
                            window.add(paddle)
                            graphics.paddle = paddle
                if buff.y > window.height:  # If buff out to window, move out from list
                    buffs.remove(buff)
                    window.remove(buff)
            if graphics.score == graphics.bricks_count:
                break

        else:
            lives -= 1
            graphics.pause_switch = True
            if lives > 0:
                graphics.reset_ball()
                vx = 0
                vy = 0
            else:
                break
        pause(FRAME_RATE)


def check_collision(obj1, obj2):
    """
    Determine whether two objects have collided.
    :param obj1: Gobject
    :param obj2: Gobject
    :return: True of False
    """
    obj1_left = obj1.x
    obj1_right = obj1.x+obj1.width
    obj1_top = obj1.y
    obj1_bottom = obj1.y+obj1.height
    obj2_left = obj2.x
    obj2_right = obj2.x+obj2.width
    obj2_top = obj2.y
    obj2_bottom = obj2.y+obj2.height
    if obj1_right > obj2_left and obj1_bottom > obj2_top and obj1_left < obj2_right and obj1_top < obj2_bottom:
        return True
    return False


if __name__ == '__main__':
    main()
