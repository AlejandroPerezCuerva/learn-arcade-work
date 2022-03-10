""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
VELOCIDAD_MOVIMIENTO= 3
DEAD_ZONE=0.02

def dibujarStickmam(coorX, coorY, color):#Las coordenadas se corresponden con el centro del stickman
    """Dibuja un stckman de proporciones ya definidas"""
    #cabeza
    arcade.draw_circle_filled(coorX, coorY+20, 10, color)
    #cuerpo
    arcade.draw_line(coorX, coorY+20, coorX, coorY-20, color, 5)
    #brazos
    arcade.draw_line(coorX, coorY+10, coorX+20, coorY-20, color, 5)
    arcade.draw_line(coorX, coorY+10, coorX-20, coorY-20, color, 5)
    #piernas
    arcade.draw_line(coorX, coorY-20, coorX+20, coorY-70, color, 5)
    arcade.draw_line(coorX, coorY-20, coorX-20, coorY-70, color, 5)

def dibujarParedes(): # Función para crear paredes que el stickman no pueda atravesar, abandonada hasta comprensión más avanzada
    arcade.draw_line(0, 5, 230, 5, arcade.color.RED, 5)
    arcade.draw_line(0, 130, 130, 130, arcade.color.RED, 5)

    arcade.draw_line(230, 5, 230, 130, arcade.color.RED, 5)
    arcade.draw_line(130, 130, 130, 280, arcade.color.RED, 5)

    arcade.draw_line(230, 130, 350, 130, arcade.color.RED, 5)
    arcade.draw_line(130, 280, 470, 280, arcade.color.RED, 5)

    arcade.draw_line(350, 130, 350, 5, arcade.color.RED, 5)
    arcade.draw_line(470, 280, 470, 130, arcade.color.RED, 5)

    arcade.draw_line(350, 5, 690, 5, arcade.color.RED, 5)
    arcade.draw_line(470, 130, 570, 130, arcade.color.RED, 5)

    arcade.draw_line(690, 5, 690, 300, arcade.color.RED, 5)
    arcade.draw_line(570, 130, 570, 300, arcade.color.RED, 5)

    arcade.draw_text("Meta", 610, 310, arcade.color.BLACK, 13)
    arcade.draw_line(570, 300, 690, 300, arcade.color.YELLOW, 5)

def dibujarFondo():
    arcade.set_background_color(arcade.color.BABY_BLUE)
class StickMan:
    def __init__(self, pos_x, pos_y, nueva_x, nueva_y, ancho, alto, color):
        self.position_x=pos_x
        self.position_y=pos_y
        self.nueva_x=nueva_x
        self.nueva_y=nueva_y
        self.ancho=ancho
        self.alto=alto
        self.color=color
        self.oof=arcade.load_sound("oof.wav")

    def draw(self):
        dibujarStickmam(self.position_x, self.position_y, self.color)

    def update(self):
        # Se actualiza la posición
        self.position_x += self.nueva_x
        self.position_y += self.nueva_y

        if self.position_x < self.ancho:
            self.position_x = self.ancho
            arcade.play_sound(self.oof)

        if self.position_x > SCREEN_WIDTH - self.ancho:
            self.position_x = SCREEN_WIDTH - self.ancho
            arcade.play_sound(self.oof)

        if self.position_y < self.alto:
            self.position_y = self.alto
            arcade.play_sound(self.oof)

        if self.position_y > SCREEN_HEIGHT - self.alto:
            self.position_y = SCREEN_HEIGHT - self.alto
            arcade.play_sound(self.oof)

class Stick:
    def __init__(self, pos_x, pos_y, nueva_x, nueva_y, ancho, alto, color):
        self.position_x=pos_x
        self.position_y=pos_y
        self.nueva_x=nueva_x
        self.nueva_y=nueva_y
        self.ancho=ancho
        self.alto=alto
        self.color=color
        self.oof=arcade.load_sound("oof.wav")


    def draw(self):
        arcade.draw_line(self.position_x, self.position_y-25,  self.position_x, self.position_y+25, self.color, 5)

    def update(self):
        # Se actualiza la posición
        self.position_x += self.nueva_x
        self.position_y += self.nueva_y

        if self.position_x < self.ancho:
            self.position_x = self.ancho
            arcade.play_sound(self.oof)

        if self.position_x > SCREEN_WIDTH - self.ancho:
            self.position_x = SCREEN_WIDTH - self.ancho
            arcade.play_sound(self.oof)

        if self.position_y < self.alto:
            self.position_y = self.alto
            arcade.play_sound(self.oof)

        if self.position_y > SCREEN_HEIGHT - self.alto:
            self.position_y = SCREEN_HEIGHT - self.alto
            arcade.play_sound(self.oof)

class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        #Se hace el puntero visible y se cargan sonidos
        self.set_mouse_visible(False)
        self.click=arcade.load_sound("click.wav")

        #Se crea el stickMan
        self.sitckManR=StickMan(60, 85, 0, 0, 25, 75, arcade.color.BLACK)
        self.stick=Stick(60, 85, 0, 0, 5, 30, arcade.color.GREEN)
        self.sitckManM=StickMan(60, 85, 0, 0, 25, 75, arcade.color.BLUE)

        #Se introducen los mandos
        joysticks = arcade.get_joysticks()

        if joysticks: #Si hay mandos, instancia la variable, si no nada
            self.joystick = joysticks[0]
            self.joystick.open()
        else:
            print("No hay mandos conectados")
            self.joystick = None

    def on_draw(self):
        dibujarFondo()
        arcade.start_render()

        self.sitckManR.draw()
        self.stick.draw()
        self.sitckManM.draw()

    def update(self, delta_time):
        self.sitckManR.update()
        self.stick.update()
        if self.joystick:
            print(self.joystick.x, self.joystick.y)
            self.sitckManM.nueva_x=self.joystick.x * 3
            self.sitckManM.nueva_y=self.joystick.y * 3
            #Se define la dead zone para dar un cierto margen al usuario
            if abs(self.joystick.x) < DEAD_ZONE:
                self.ball.change_x = 0
            else:
                self.ball.change_x = self.joystick.x * VELOCIDAD_MOVIMIENTO

            # Set a "dead zone" to prevent drive from a centered joystick
            if abs(self.joystick.y) < DEAD_ZONE:
                self.ball.change_y = 0
            else:
                self.ball.change_y = -self.joystick.y * VELOCIDAD_MOVIMIENTO


    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.sitckManR.position_x = x
        self.sitckManR.position_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        """ Called when the user presses a mouse button. """

        if button == arcade.MOUSE_BUTTON_LEFT:
            print("Click izquierdo")
            arcade.play_sound(self.click)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            print("Click derecho")
            arcade.play_sound(self.click)

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.stick.nueva_x = -VELOCIDAD_MOVIMIENTO
        elif key == arcade.key.RIGHT:
            self.stick.nueva_x = VELOCIDAD_MOVIMIENTO
        elif key == arcade.key.UP:
            self.stick.nueva_y = VELOCIDAD_MOVIMIENTO
        elif key == arcade.key.DOWN:
            self.stick.nueva_y = -VELOCIDAD_MOVIMIENTO

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.stick.nueva_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.stick.nueva_y = 0

def main():
    window = MyGame()
    arcade.run()


main()