import arcade


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def on_draw(self):


        arcade.start_render()


class Balle():
    def __init__(self, ):
        self.x = 15
        self.y = 15
        self.change_x = 3
        self.change_y = 3
        self.rayon = 10


    def on_draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.rayon, (255, 54, 34))


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




class Rectanlge():







def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Tutoriel Arcade")
    arcade.run()



main()
Balle()
