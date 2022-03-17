""" Lab 8 - Sprites """
import random
import arcade

ESCALADO_SPRITE_NAVE = 0.6
ESCALADO_SPRITE_MONEDA_GRANDE=0.5
ESCALADO_SPRITE_MONEDA:PEQUENNA = 0.3
N_MONEDAS = 40
ESCALADO_SPRITE_METEORITO = 0.5
N_METEORITOS = 20

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
class Meteorito(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):

        # Move the coin
        self.center_x += self.change_x
        self.center_y += self.change_y

        # If we are out-of-bounds, then 'bounce'
        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1

class Moneda(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0
        self.pulso_grande=True

    def update(self):

        # Move the coin

        # La moneda toma un tamaño u otro por turnos
        if(self.pulso_grande==True):
            self.pulso_grande=False
        else:
            self.pulso_grande = True
class MyGame(arcade.Window):
    def __init__(self):
        """ Inicializador """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprites")

        #Atributos de los sprites
        self.lista_jugador = None
        self.lista_monedas = None
        self.lista_meteoritos = None

        # Atributos del jugador
        self.sprite_jugador = None
        self.puntos = 0

        #Mouse invisible y se pausa si no esta en la ventana
        self.set_mouse_visible(False)
        self.mouse_fuera_ventana = False

        #Carga de sonidos al colisionar
        self.coin=arcade.load_sound("arcade_resources_sounds_coin5.wav")
        self.hit=arcade.load_sound("arcade_resources_sounds_error5.wav")
        arcade.set_background_color(arcade.color.SKY_BLUE)

    def setup(self):
        """ Creación de sprites y atributos """

        # Listas de sprites
        self.lista_jugador = arcade.SpriteList()
        self.lista_monedas = arcade.SpriteList()
        self.lista_meteoritos = arcade.SpriteList()

        self.puntos = 0

        # Instanciación del sprite del jugador
        self.sprite_jugador = arcade.Sprite("playerShip2_orange.png", ESCALADO_SPRITE_NAVE)
        self.sprite_jugador.center_x  = 50
        self.sprite_jugador.center_y  = 50
        self.lista_jugador.append(self.sprite_jugador)

        #Creación e inicialización de las monedas
        for i in range(N_MONEDAS):
            #Creación de la moneda
            if(pulso_grande==True)
                moneda = Moneda("coinGold.png", ESCALADO_SPRITE_MONEDA_GRANDE)
            else:
                moneda = Moneda("coinGold.png", ESCALADO_SPRITE_MONEDA_PEQUENNA)

            #Instanciación de la moneda
            moneda.center_x = random.randrange(SCREEN_WIDTH)
            moneda.center_y = random.randrange(SCREEN_HEIGHT)
            moneda=


        #Creación e inicialización de los meteoritos
        for j in range(N_METEORITOS):
            # Creación del meteorito
            meteorito = Meteorito("meteorGrey_small2.png", ESCALADO_SPRITE_METEORITO)

            # Instanciación del meteorito
            meteorito.center_x = random.randrange(SCREEN_WIDTH)
            meteorito.center_y = random.randrange(SCREEN_HEIGHT)
            meteorito.change_x = random.randrange(-3, 4)
            meteorito.change_y = random.randrange(-3, 4)

            self.lista_meteoritos.append(meteorito)

    def on_draw(self):
        arcade.start_render()

        self.lista_monedas.draw()
        self.lista_meteoritos.draw()
        self.lista_jugador.draw()

        puntos_hud = f"Score: {self.puntos}"
        arcade.draw_text(puntos_hud, 10, 20, arcade.color.BLACK, 12)

    def on_mouse_motion(self, x, y, dx, dy):

        self.sprite_jugador.center_x = x
        self.sprite_jugador.center_y = y
        if(x>SCREEN_WIDTH or y>SCREEN_HEIGHT):
            self.mouse_fuera_ventana= True
        else:
            self.mouse_fuera_ventana= False

    def update(self, delta_time):
        """ Movimiento y colisiones """
        if(not self.mouse_fuera_ventana):
            # Actualiza todos los sprites
            self.lista_monedas.update()
            self.lista_meteoritos.update()

            # Se genera una lista con todas las colisiones
            colisiones_monedas = arcade.check_for_collision_with_list(self.sprite_jugador, self.lista_monedas)
            colisiones_meteoritos = arcade.check_for_collision_with_list(self.sprite_jugador, self.lista_meteoritos)

            # Si un sprite colisiona, se elimina
            for moneda in colisiones_monedas:
                moneda.remove_from_sprite_lists()
                self.puntos += 1
                arcade.play_sound(self.coin)

            for meteorito in colisiones_meteoritos:
                meteorito.remove_from_sprite_lists()
                self.puntos += -1
                arcade.play_sound(self.hit)


def main():
    """ Main  """
    window = MyGame()
    window.setup()
    arcade.run()

main()
