'''
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.

My choice is to depict dogs in a mall

'''

import arcade
import random

class Pooch:
    def __init__(self):
        self.size = random.randint(10, 51)
        self.x = random.randint(30 + (2 * self.size), 571 - (2 * self.size))
        self.y = 600
        self.dx = random.randint(-300, 301)
        self.dy = random.randint(-300, 301)
        shades = [arcade.csscolor.BEIGE, arcade.csscolor.BURLYWOOD, arcade.csscolor.DARK_GREY]
        self.shade = shades[random.randint(0, 2)]

    def draw_pooch(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.size, self.size, self.shade)

    def update_pooch(self, dt):
        self.x += self.dx * dt
        self.y += self.dy * dt


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.csscolor.GAINSBORO)
        self.w = width
        self.h = height
        self.box_list = []
        for i in range(30):
            box = Pooch()
            self.box_list.append(box)

    def on_draw(self):
        arcade.start_render()
        for box in self.box_list:
            box.draw_pooch()

    def on_update(self, dt):
        for box in self.box_list:
            box.update_pooch(dt)

def main():
    window = MyGame(600, 600, "Dogs in a mall")
    arcade.run()

if __name__ == "__main__":
    main()