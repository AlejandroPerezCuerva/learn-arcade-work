import arcade

def dibujarRectangulo(coorX, coorY, ancho, alto, color):
    """ Dibuja un rectángulo"""
    arcade.draw_lrtb_rectangle_filled(coorX-ancho/2, coorX+ancho/2, coorY+alto/2, coorY-alto/2, color)

def dibujarMoneda(coorX, coorY):
    """ Dibuja una moneda"""
    arcade.draw_circle_filled(coorX, coorY, 20, arcade.color.OLD_GOLD)
    arcade.draw_circle_filled(coorX, coorY, 15, arcade.color.GOLD)
  #  arcade.draw_text("5P", coorX-10, coorY-8, arcade.color.BLACK, 13)
  #por algún motivo que no logro comprender el texto sale mal, en forma de manchurrón en medio de la pantalla, por lo que lo dejo comentado hasta que lo solucione

def dibujarTriangulo(coorX, coorY, color, direccion):#Las coordenadas se corresponden con el centro del triangulo
    """Dibuja un triángulo. Los triángulos tendrán un tamaño predeterminado, pudiendo elegir el color, la posición y si apunta arriba o abajo"""
    X1=coorX-15
    X2=coorX+15
    X3=(X1+X2)/2
    if direccion==1:#apunta arriba
        arcade.draw_triangle_filled(X1, coorY, X2, coorY, X3, coorY+25, color)
    elif direccion==0:
        arcade.draw_triangle_filled(X1, coorY, X2, coorY, X3, coorY-25, color)

def dibujarCorazon(coorX, coorY, color):#Las coordenadas se corresponden con el centro del corazón
    """Dibuja un corazón, los corazones tienen unas proporciones predefinidas"""
    dibujarTriangulo(coorX, coorY, color, 0)
    arcade.draw_arc_filled(coorX-7, coorY, 17, 21, color, 0, 180)
    arcade.draw_arc_filled(coorX+7, coorY, 17, 21, color, 0, 180)


#def dibujarBandera():

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

def main():
    arcade.open_window(800, 600, "Ejemplo dibujo")

    # Se limpia el fondo e inicia el render
    arcade.set_background_color(arcade.color.DARK_POWDER_BLUE)
    arcade.start_render()
    #Se dibuja la ventana
    #vida 1
    dibujarCorazon(25, 570, arcade.csscolor.RED)
    #vida 2
    dibujarCorazon(60, 570, arcade.csscolor.RED)
    #vida 3, vida perdida
    dibujarCorazon(95, 570, arcade.csscolor.BLACK)

    #se dibujan las plataformas
    dibujarRectangulo(100, 50, 200, 100, arcade.color.BLACK);
    dibujarRectangulo(475, 25, 150, 50, arcade.color.BLACK);
    dibujarRectangulo(725, 25, 150, 50, arcade.color.BLACK);

    #bandera
    dibujarRectangulo(755, 110, 10, 120, arcade.color.WHITE);
    dibujarRectangulo(740, 155, 40, 30, arcade.color.YELLOW);

    #monigote stickman: cabeza->cuerpo->brazos->piernas, en ese orden
    dibujarStickmam(70, 150, arcade.color.BLACK)

    #lava
    dibujarRectangulo(301, 10, 200, 20, arcade.color.LUST)

   # dibujarRectangulo(201, 399, 20, 0, arcade.color.LUST)
    #pinchos
    dibujarTriangulo(510, 50, arcade.csscolor.GRAY, 1)
    dibujarTriangulo(665, 50, arcade.csscolor.GRAY, 1)
    #moneda
    dibujarMoneda(300, 250)

    #Se termina el render
    arcade.finish_render()

    #se mantiene la ventana abierta
    arcade.run()

main()