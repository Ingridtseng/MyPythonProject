"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel, GArc, GLine
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball
start_ball = False


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=window_width/2 - paddle_width/2, y=window_height - paddle_offset - paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=window_width/2 - ball_radius, y=window_height/2 - ball_radius)
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # the total amount of bricks
        self.numbricks = brick_rows*brick_cols

        # Initialize our mouse listeners
        onmousemoved(self.paddle_animation)
        onmouseclicked(self.ball_status)

        # Draw bricks
        for i in range(brick_cols):
            for j in range(brick_rows):
                self.bricks = GRect(brick_width, brick_height, x=i*(brick_width+brick_spacing), y=brick_offset+j*(brick_height+brick_spacing))
                color_range = brick_rows/5
                if j <= color_range-1:
                    self.bricks.filled = True
                    self.bricks.fill_color = 'red'
                elif color_range-1 < j <= 2*color_range-1:
                    self.bricks.filled = True
                    self.bricks.fill_color = 'orange'
                elif 2*color_range-1 < j <= 3*color_range-1:
                    self.bricks.filled = True
                    self.bricks.fill_color = 'yellow'
                elif 3*color_range-1 < j <= 4*color_range-1:
                    self.bricks.filled = True
                    self.bricks.fill_color = 'green'
                elif 4*color_range-1 < j <= BRICK_ROWS:
                    self.bricks.filled = True
                    self.bricks.fill_color = 'blue'
                self.window.add(self.bricks)

    def paddle_animation(self, mouse):
        if 0+self.paddle.width/2 < mouse.x < self.window.width-self.paddle.width/2:
            self.paddle.x = mouse.x - self.paddle.width/2
        elif mouse.x > self.window.width-self.paddle.width/2:
            self.paddle.x = self.window.width-self.paddle.width
        else:
            self.paddle.x = 0

    def ball_status(self, click):
        global start_ball
        start_ball = True

    def ball_animation(self):
        global start_ball
        if start_ball:
            self.__dy = -INITIAL_Y_SPEED
            self.__dx = random.randint(1, MAX_X_SPEED+1)
            if random.random() > 0.5:
                self.__dx = -self.__dx
            self.ball.move(self.__dx, self.__dy)
            start_ball = False

    def get_dx(self):
        return self.__dx

    def set_dx(self, dx):
        self.__dx = dx

    def get_dy(self):
        return self.__dy

    def set_dy(self, dy):
        self.__dy = dy

    def get_ball_diameter(self):
        return self.ball.width




