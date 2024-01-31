import random

import arcade


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

Colours = [arcade.color.VIOLET, arcade.color.GREEN, arcade.color.RED, arcade.color.BLUE, arcade.color.YELLOW, arcade.color.ORANGE]

class Balle():
    def __init__(self,x, y):
        self.x = x
        self.y = y
        self.change_x = random.randint(-4, 4)
        self.change_y = random.randint(-4, 4)
        self.rayon = 10
        self.color = random.choice(Colours)


    def on_draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.rayon, color=self.color)


    def on_update(self):
        self.x += self.change_x
        self.y += self.change_y
        if self.x < self.rayon:
            self.change_x *= -1
        if self.x > SCREEN_WIDTH - self.rayon:
            self.change_x *= -1
        if self.y < self.rayon:
            self.change_y *= -1
        if self.y > SCREEN_HEIGHT - self.rayon:
            self.change_y *= -1





class Rectangle():

    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.change_x = random.randint(-4, 4)
        self.change_y = random.randint(-4, 4)
        self.color = random.choice(Colours)
        self.height = random.randint(10, 30)
        self.width = random.randint(10, 30)
        self.angle = random.randint(0, 90)


    def on_draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, color=self.color, tilt_angle=self.angle)


    def on_update(self):
        self.x += self.change_x
        self.y += self.change_y
        if self.x < self.height:
            self.change_x *= -1
        if self.x > SCREEN_WIDTH - self.width:
            self.change_x *= -1
        if self.y < self.height:
            self.change_y *= -1
        if self.y > SCREEN_HEIGHT - self.height:
            self.change_y *= -1










class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.liste_balles = []
        self.liste_rectangles = []

    def on_draw(self):
        arcade.start_render()
        for i in self.liste_balles:
            i.on_draw()
        for i in self.liste_rectangles:
            i.on_draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            balle_1 = Balle(x, y)
            self.liste_balles.append(balle_1)

        elif button == arcade.MOUSE_BUTTON_RIGHT:
            rectangle_1 = Rectangle(x, y)
            self.liste_rectangles.append(rectangle_1)

    def on_update(self, delta_time: float):
        for i in self.liste_balles:
            i.on_update()
        for i in self.liste_rectangles:
            i.on_update()






def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Tutoriel Arcade")
    arcade.run()



main()

