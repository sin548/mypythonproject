"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

Added a scoreboard on top of the original setup, where the speed increases every 10 points.
Also added two buffs: when a brick disappears, two rectangles are randomly generated,
which will either increase or decrease the paddle's length.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 100      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 5    # Initial vertical speed for the ball
MAX_X_SPEED = 4        # Maximum initial horizontal speed for the ball
RECT_WIDTH = 15        # Width of the rect (in pixels)


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 rect_width=RECT_WIDTH, title='Breakout'):

        self.paddle_width = paddle_width
        self.ball_radius = ball_radius
        self.bricks_count = BRICK_ROWS * BRICK_COLS
        self.paddle_height = paddle_height

        # Create a graphical window, with some extra space
        self.window_width = brick_rows * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_cols * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(self.paddle_width, paddle_height, x=(self.window_width-self.paddle_width)//2,
                       y=self.window_height-paddle_offset-paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=(self.window_width-ball_radius)//2, y=(self.window_height-ball_radius)//2)
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = INITIAL_Y_SPEED

        # Initialize our mouse listeners
        onmousemoved(self.on_mouse_moved)
        onmouseclicked(self.start)
        self.pause_switch = True   # True is locked

        # Create scoreboard
        self.score = 0
        self.scoreboard = GLabel("Score: "+str(self.score), x=0, y=self.window_height)
        self.scoreboard.font = '-20'
        self.window.add(self.scoreboard)

        # Draw bricks
        for i in range(brick_rows):
            for j in range(brick_cols):
                brick = GRect(brick_width, brick_height, x=i*(brick_width+brick_spacing),
                              y=brick_offset+j*(brick_height+brick_spacing))
                brick.filled = True
                if j < 2:
                    brick.fill_color = "red"
                elif j < 4:
                    brick.fill_color = "orange"
                elif j < 6:
                    brick.fill_color = "yellow"
                elif j < 8:
                    brick.fill_color = "green"
                elif j < 10:
                    brick.fill_color = "blue"
                self.window.add(brick)

        # Crate buff pattern
        self.rect1 = GRect(rect_width, rect_width)
        self.rect1.filled = True
        self.rect1.color = 'lightgreen'
        self.rect1.fill_color = 'lightgreen'
        self.rect2 = GRect(rect_width, rect_width)
        self.rect2.filled = True
        self.rect2.color = 'lightgray'
        self.rect2.fill_color = 'lightgray'

    def random_buff(self):
        """
        Randomly return rect1, rect2, or nothing at all. And the probability of nothing at all is 60%.
        :return: object
        """
        result = random.randint(1, 5)
        if result == 1:
            return self.rect1
        elif result == 2:
            return self.rect2
        else:
            return 0

    def start(self, event):
        """
        Throw out a random dx speed, and turn on the switch to allow the while loop on the user side to proceed.
        """
        if self.pause_switch:
            dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                dx = -dx
            self.__dx = dx
            self.__dy = INITIAL_Y_SPEED
            self.pause_switch = False  # False is open

    def get_vx(self):
        return self.__dx

    def get_vy(self):
        return self.__dy

    def on_mouse_moved(self, event):
        """
        The X position of the paddle will follow the mouse movement and be restricted within the window boundaries.
        """
        new_x = event.x - self.paddle_width // 2
        if 0 <= new_x <= self.window_width-self.paddle_width:
            self.paddle.x = new_x
        # When the mouse leaves the window, the paddle will snap directly to the far left or far right edge.
        elif new_x < 0:
            self.paddle.x = 0
        elif new_x > self.window_width-self.paddle_width:
            self.paddle.x = self.window_width-self.paddle_width

    def reset_ball(self):
        self.ball.x = (self.window_width - self.ball_radius)//2
        self.ball.y = (self.window_height - self.ball_radius)//2
