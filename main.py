def on_button_pressed_a():
    global timer
    timer = 0
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global pause2, timer
    pause2 = timer
    basic.clear_screen()
    basic.show_icon(IconNames.NO)
    basic.pause(120000)
    basic.clear_screen()
    timer = pause2
input.on_button_pressed(Button.B, on_button_pressed_b)

pause2 = 0
timer = 0
timer = 0
pause2 = 0
basic.show_string("GO")

def on_forever():
    global timer
    timer += 1
    if timer <= 25:
        led.plot_bar_graph(timer, 25)
    else:
        basic.clear_screen()
        for index in range(3):
            basic.clear_screen()
            basic.show_icon(IconNames.YES)
            basic.pause(100)
    basic.pause(60000)
basic.forever(on_forever)
