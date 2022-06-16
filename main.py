numero1 = 0
numero2 = 0

def on_button_pressed_a():
    global numero1, numero2
    numero1 = randint(1, 10)
    basic.show_number(numero1)
    basic.pause(500)
    basic.show_leds("""
        . . # . .
                . . # . .
                # # # # #
                . . # . .
                . . # . .
    """)
    numero2 = randint(1, 10)
    basic.show_number(numero2)
    basic.pause(500)
    basic.show_leds("""
        . . . . .
                # # # # #
                . . . . .
                # # # # #
                . . . . .
    """)
    basic.pause(1000)
    basic.show_number(numero1 + numero2)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global numero1, numero2
    numero1 = randint(1, 10)
    basic.show_number(numero1)
    basic.pause(500)
    basic.show_leds("""
        . . . . .
                . . . . .
                # # # # #
                . . . . .
                . . . . .
    """)
    numero2 = randint(1, 10)
    basic.show_number(numero2)
    basic.pause(500)
    basic.show_leds("""
        . . . . .
                # # # # #
                . . . . .
                # # # # #
                . . . . .
    """)
    basic.pause(1000)
    basic.show_number(numero1 - numero2)
input.on_button_pressed(Button.B, on_button_pressed_b)
