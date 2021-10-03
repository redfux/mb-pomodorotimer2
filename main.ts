input.onButtonPressed(Button.A, function () {
    timer = 0
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    pause2 = timer
    basic.clearScreen()
    basic.showIcon(IconNames.No)
    basic.pause(120000)
    basic.clearScreen()
    timer = pause2
})
let pause2 = 0
let timer = 0
timer = 0
pause2 = 0
basic.showString("GO")
basic.forever(function () {
    basic.clearScreen()
    timer += 1
    if (timer <= 25) {
        led.plotBarGraph(
        timer,
        25
        )
    } else {
        basic.clearScreen()
        for (let index = 0; index < 3; index++) {
            basic.clearScreen()
            basic.showIcon(IconNames.Yes)
            basic.pause(100)
        }
    }
    basic.pause(60000)
})
