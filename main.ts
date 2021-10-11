input.onButtonPressed(Button.A, function () {
    control.reset()
})
input.onButtonPressed(Button.B, function () {
    unterbrechung += 1
    basic.showIcon(IconNames.No)
})
let effektivitaet = 0
let Index = 0
let timer = 0
let unterbrechung = 0
basic.showString("GO")
basic.forever(function () {
    basic.clearScreen()
    if (timer <= 25) {
        led.plotBarGraph(
        timer,
        25
        )
    } else {
        basic.clearScreen()
        effektivitaet = 100 - unterbrechung / 0.25
        for (let index = 0; index < 3; index++) {
            if (effektivitaet == 100) {
                basic.clearScreen()
                basic.showIcon(IconNames.Yes)
                basic.pause(100)
            } else {
                basic.clearScreen()
                basic.showString("" + effektivitaet + "%")
                basic.showIcon(IconNames.Sad)
                basic.pause(100)
            }
        }
    }
    for (let Index = 0; Index <= 60; Index++) {
        basic.pause(1000)
    }
    Index = 0
    timer += 1
})
