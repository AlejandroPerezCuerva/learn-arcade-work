""" Sprites y Muros"""

import random
import arcade
from pyglet.math import Vec2

SPRITE_SCALING = 0.5
COIN_SCALING = 0.3

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Scrolling Screen Example"

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 220

# How fast the camera pans to the player. 1.0 is instant.
CAMERA_SPEED = 0.1

# How fast the character moves
PLAYER_MOVEMENT_SPEED = 7


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True)

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.lista_monedas = None

        # Set up the player
        self.player_sprite = None
        self.puntos = 0

        # Physics engine so we don't run into walls.
        self.physics_engine = None

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # Create the cameras. One for the GUI, one for the sprites.
        # We scroll the 'sprite world' but not the GUI.
        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

        #Cargo el sonido de recoger moneda
        self.coin=arcade.load_sound("arcade_resources_sounds_coin5.wav")

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.lista_monedas = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite("mouse.png",
                                           scale=0.4)
        self.player_sprite.center_x = 256
        self.player_sprite.center_y = 512
        self.player_list.append(self.player_sprite)

        # -- Se cierra la habitación poniendo tierra en un cuadrado
        for x in range(0, 1650, 64):
            y=0;
            wall = arcade.Sprite("stone.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = y
            self.wall_list.append(wall)
            y = 1600; #Se aprovecha cada iteración para poner tierra de techo y otra de suelo
            wall = arcade.Sprite("stone.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = y
            self.wall_list.append(wall)
        for y in range(0, 1600, 64):
            x=0;
            wall = arcade.Sprite("stone.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = y
            self.wall_list.append(wall)
            x = 1650; #Se aprovecha cada iteración para poner tierra a la derecha e izquierda
            wall = arcade.Sprite("stone.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = y
            self.wall_list.append(wall)

        #se ponen las paredes de la habitación

        for x in range(64, 1586, 128):
            for y in range(64, 1536, 128):
                #Es de distinta textura pero eslo mismo, asi que se reutiliza wall
                if random.randrange(100) > 70:
                    wall = arcade.Sprite("dirt.png", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)
                elif random.randrange(100) > 70:
                    wall = arcade.Sprite("grass.png", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)
                else:
                    wall = arcade.Sprite("sandCenter_rounded.png", SPRITE_SCALING)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)

        for x in range(128, 1586, 128):
            for y in range(128, 1536, 128):
                if random.randrange(100) > 60:
                    # Creación de las monedas
                    moneda = arcade.Sprite("coinGold.png", COIN_SCALING)
                    # Instanciación de la moneda
                    moneda.center_x = x
                    moneda.center_y = y
                    self.lista_monedas.append(moneda)



        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.GRAY)

    def on_draw(self):
        """ Render the screen. """

        # This command has to happen before we start drawing
        self.clear()

        # Select the camera we'll use to draw all our sprites
        self.camera_sprites.use()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.lista_monedas.draw()

        # Select the (unscrolled) camera for our GUI
        self.camera_gui.use()

        # Draw the GUI
        arcade.draw_rectangle_filled(self.width // 2,
                                     20,
                                     self.width,
                                     40,
                                     arcade.color.ALMOND)
        text = f"Scroll value: ({self.camera_sprites.position[0]:5.1f}, " \
               f"{self.camera_sprites.position[1]:5.1f})"
        arcade.draw_text(text, 10, 10, arcade.color.BLACK_BEAN, 20)

        puntos_hud = f"Score: {self.puntos}"
        arcade.draw_text(puntos_hud, 700, 20, arcade.color.BLACK, 12)
    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        # Scroll the screen to the player
        self.scroll_to_player()

        #Se actualizan las monedas y las colisiones
        self.lista_monedas.update()
        colisiones_monedas = arcade.check_for_collision_with_list(self.player_sprite, self.lista_monedas)
        for moneda in colisiones_monedas:
            moneda.remove_from_sprite_lists()
            self.puntos += 1
            arcade.play_sound(self.coin)

    def scroll_to_player(self):
        """
        Scroll the window to the player.

        if CAMERA_SPEED is 1, the camera will immediately move to the desired position.
        Anything between 0 and 1 will have the camera move to the location with a smoother
        pan.
        """

        position = Vec2(self.player_sprite.center_x - self.width / 2,
                        self.player_sprite.center_y - self.height / 2)
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):
        """
        Resize window
        Handle the user grabbing the edge and resizing the window.
        """
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))


def main():
    """ Main function """
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()