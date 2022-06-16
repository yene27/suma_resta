let numero1 = 0
let numero2 = 0
input.onButtonPressed(Button.A, function () {
    numero1 = randint(1, 10)
    basic.showNumber(numero1)
    basic.pause(500)
    basic.showLeds(`
        . . # . .
        . . # . .
        # # # # #
        . . # . .
        . . # . .
        `)
    numero2 = randint(1, 10)
    basic.showNumber(numero2)
    basic.pause(500)
    basic.showLeds(`
        . . . . .
        # # # # #
        . . . . .
        # # # # #
        . . . . .
        `)
    basic.pause(1000)
    basic.showNumber(numero1 + numero2)
    basic.pause(1000)
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    numero1 = randint(1, 10)
    basic.showNumber(numero1)
    basic.pause(500)
    basic.showLeds(`
        . . . . .
        . . . . .
        # # # # #
        . . . . .
        . . . . .
        `)
    numero2 = randint(1, 10)
    basic.showNumber(numero2)
    basic.pause(500)
    basic.showLeds(`
        . . . . .
        # # # # #
        . . . . .
        # # # # #
        . . . . .
        `)
    basic.pause(1000)
    basic.showNumber(numero1 - numero2)
    basic.pause(1000)
    basic.clearScreen()
})
