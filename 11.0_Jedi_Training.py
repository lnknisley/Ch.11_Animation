'''
# 11.0 Jedi Training (50pts)  Name:________________



 
CHAPTER 11 FINAL CODE QUESTIONS: (10pts)
--------------------------------
1.) Where is the ball's original location?
It's randomized
2.) What are the variables dx and dy?
The change in the x and change in the y added each frame
3.) How many pixels/sec does the ball move in the x-direction?
At best +/-300 pixels per second
4.) How many pixels/sec does the ball move in the y-direction?
At best +/-300 pixels per second
5.) Which method is run 60 times/second?
The update method
6.) What does this code do?   self.dx *= -1
It reverses the direction of the ball's x
7.) What does this code do?  self.pos_y += self.dy
It adds the dy, the change in y, to the ball's y value
8.) What is the width of the window?
600
9.) What is this code checking?  self.pos_y > SH - self.rad:
If the position of the box is touching the top of the screen
10.) What is this code checking? if self.pos_x < self.rad
if the position of the box is touching the left of the screen
'''
from arcade import draw_rectangle_filled

'''
30 BOX BOUNCE PROGRAM (20pts)
---------------------
You will want to incorporate lists to modify the
Ball Bounce Program to create the following:

1.) Screen size 600 x 600
2.) Draw four 30px wide side rails on all four sides of the window
3.) Make each side rail a different color.
4.) Draw 30 black boxes(squares) of random size from 10-50 pixels
5.) Animate them starting at random speeds from -300 to +300 pixels/second. 
6.) All boxes must be moving.
7.) Start all boxes in random positions between the rails.
8.) Bounce boxes off of the side rails when the box edge hits the side rail.
9.) When the box bounces change its color to the rail it just hit.
10.)Title the window 30 Boxes

Helpful Hints:
1.) When you initialize the MyGame class create an empty list called self.boxlist=[] to hold all of your boxes.
2.) Then use a for i in range(30): list to instantiate boxes and append them to the list.
3.) In the on_draw section use: for box in self.boxlist: box.draw_box()
4.) Also in the on_draw section draw the side rails.
5.) In the on_update section use: for box in self.boxlist: box.update_box()
'''


import arcade
import random

class Box:
    def __init__(self, col_1, col_2, col_3, col_4):
        self.size = random.randint(10, 51)
        self.x = random.randint(30 + (2 * self.size), 571 - (2 * self.size))
        self.y = random.randint(30 + (2 * self.size), 571 - (2 * self.size))
        self.dx = random.randint(-300, 301)
        self.dy = random.randint(-300, 301)
        self.color = arcade.color.BLACK
        self.color_bottom = col_1
        self.color_top = col_2
        self.color_left = col_3
        self.color_right = col_4

    def draw_box(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.size, self.size, self.color)

    def update_box(self, dt):
        if self.x <= 29 + (self.size * 0.5):
            self.dx *= -1
            self.color = self.color_left
        if self.x >= 571 - (self.size * 0.5):
            self.dx *= -1
            self.color = self.color_right
        if self.y <= 29 + (self.size * 0.5):
            self.dy *= -1
            self.color = self.color_bottom
        if self.y >= 571 - (self.size * 0.5):
            self.dy *= -1
            self.color = self.color_top

        self.x += self.dx * dt
        self.y += self.dy * dt


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.w = width
        self.h = height
        self.c1 = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
        self.c2 = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
        self.c3 = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
        self.c4 = (random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
        self.box_list = []
        for i in range(30):
            box = Box(self.c1, self.c2, self.c3, self.c4)
            self.box_list.append(box)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(self.w / 2, 15, self.w - 60, 30, self.c1, 0)
        arcade.draw_rectangle_filled(self.w / 2, self.h - 15, self.w - 60, 30, self.c2, 0)
        arcade.draw_rectangle_filled(15, self.h / 2, 30, self.h - 60, self.c3, 0)
        arcade.draw_rectangle_filled(self.h - 15, self.h / 2, 30, self.h - 60, self.c4, 0)
        for box in self.box_list:
            box.draw_box()

    def on_update(self, dt):
        for box in self.box_list:
            box.update_box(dt)

def main():
    window = MyGame(600, 600, "30 Boxes")
    arcade.run()

if __name__ == "__main__":
    main()

'''
SNOWFALL  (20pts)
--------
Try to create the snowfall animation by meeting
the following requirements:

1.) Create a 600 x 600 window with black background
2.) Window title equals "Snowfall"
3.) Crossbars 10 px wide. Snow must be outside!
4.) Make snowflake radius random between 1-3
5.) Randomly start snowflakes anywhere in the window.
6.) Random downward speed of -4 to -1
7.) Start snowflakes again at random x from 0-600 and random y from 600-700
8.) Generate 300 snowflakes
9.) Color snowflake #1 red just for fun.
10.) All other snowflakes should be white.
'''

class Snowflake:
    def __init__(self, color):
        self.rad = random.randint(1, 3)
        self.x = random.randint(self.rad, 601 - self.rad)
        self.y = random.randint(self.rad, 701 - self.rad)
        self.dy = random.randint(1, 4)
        self.color = color

    def draw_snowflake(self):
        arcade.draw_circle_filled(self.x, self.y, self.rad, self.color, 0, 6)

    def update_snowflake(self):
        self.y -= self.dy
        if self.y < -4:
            self.y = 628

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.w = width
        self.h = height
        self.flakes = []
        for i in range(300):
            if i == 0:
                snow = Snowflake(arcade.color.RED)
                self.flakes.append(snow)
            else:
                snow = Snowflake(arcade.color.WHITE)
                self.flakes.append(snow)

    def on_draw(self):
        arcade.start_render()
        for snow in self.flakes:
            snow.draw_snowflake()
        draw_rectangle_filled(self.w * 0.5, self.h * 0.5, self.w, 10, arcade.color.BURLYWOOD)
        draw_rectangle_filled(self.w * 0.5, self.h * 0.5, 10, self.h, arcade.color.BURLYWOOD)

    def on_update(self, dt):
        for snow in self.flakes:
            snow.update_snowflake()

def main():
    window = MyGame(600, 600, "Snowfall")
    arcade.run()

if __name__ == "__main__":
    main()