import arcade

arcade.open_window(800, 600, "Ejemplo dibujo")

# Se limpia el fondo e inicia el render
arcade.set_background_color(arcade.color.DARK_POWDER_BLUE)
arcade.start_render()
#Se dibuja
#vida 1
arcade.draw_triangle_filled(10, 570, 40, 570, 25, 545, arcade.csscolor.RED)
arcade.draw_arc_filled(18, 570, 17, 21, arcade.csscolor.RED, 0, 180)
arcade.draw_arc_filled(32, 570, 17, 21, arcade.csscolor.RED, 0, 180)
#vida 2
arcade.draw_triangle_filled(45, 570, 75, 570, 60, 545, arcade.csscolor.RED)
arcade.draw_arc_filled(53, 570, 17, 21, arcade.csscolor.RED, 0, 180)
arcade.draw_arc_filled(67, 570, 17, 21, arcade.csscolor.RED, 0, 180)
#vida 3, vida perdida
arcade.draw_triangle_filled(80, 570, 110, 570, 95, 545, arcade.csscolor.BLACK)
arcade.draw_arc_filled(88, 570, 17, 21, arcade.csscolor.BLACK, 0, 180)
arcade.draw_arc_filled(102, 570, 17, 21, arcade.csscolor.BLACK, 0, 180)

#se dibujan las plataformas
arcade.draw_lrtb_rectangle_filled(0, 200, 100, 0, arcade.color.BLACK)
arcade.draw_lrtb_rectangle_filled(400, 550, 50, 0, arcade.color.BLACK)
arcade.draw_lrtb_rectangle_filled(650, 800, 50, 0, arcade.color.BLACK)

#bandera
arcade.draw_lrtb_rectangle_filled(750, 760, 170, 50, arcade.color.WHITE)
arcade.draw_lrtb_rectangle_filled(720, 760, 170, 140, arcade.color.YELLOW)

#monigote stickman: cabeza->cuerpo->brazos->piernas, en ese orden
arcade.draw_circle_filled(70, 170, 10, arcade.color.BLACK)
arcade.draw_line(70, 170, 70, 130, arcade.color.BLACK, 5)
arcade.draw_line(70, 160, 90, 130, arcade.color.BLACK, 5)
arcade.draw_line(70, 160, 50, 130, arcade.color.BLACK, 5)
arcade.draw_line(70, 130, 50, 80, arcade.color.BLACK, 5)
arcade.draw_line(70, 130, 90, 80, arcade.color.BLACK, 5)

#lava
arcade.draw_lrtb_rectangle_filled(201, 399, 20, 0, arcade.color.LUST)
#pincho
arcade.draw_triangle_filled(500, 50, 520, 50, 510, 70, arcade.csscolor.GRAY)
arcade.draw_triangle_filled(650, 50, 670, 50, 660, 70, arcade.csscolor.GRAY)
#moneda
arcade.draw_circle_filled(300, 250, 20, arcade.color.OLD_GOLD)
arcade.draw_circle_filled(300, 250, 15, arcade.color.GOLD)
arcade.draw_text("5P", 290, 242, arcade.color.BLACK, 13)

#Se termina el render
arcade.finish_render()

#se mantiene la ventana abierta
arcade.run()