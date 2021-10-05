def on_button_pressed_a():
    control.reset()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global unterbrechung
    unterbrechung += 1
    basic.show_icon(IconNames.NO)
    basic.pause(30000)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

effektivitaet = 0
timer = 0
pause2 = 0
unterbrechung = 0
basic.show_string("GO")

def on_forever():
    global effektivitaet, timer
    basic.clear_screen()
    if timer <= 25:
        led.plot_bar_graph(timer, 25)
    else:
        basic.clear_screen()
        effektivitaet = 100 - unterbrechung / 0.125
        for index in range(3):
            if effektivitaet == 100:
                basic.clear_screen()
                basic.show_icon(IconNames.YES)
                basic.pause(100)
            else:
                basic.clear_screen()
                basic.show_string("" + str(effektivitaet) + "%")
                basic.show_icon(IconNames.SAD)
                basic.pause(100)
    basic.pause(1000)
    timer += 1
basic.forever(on_forever)
