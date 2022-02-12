def on_button_pressed_a():
    basic.show_icon(IconNames.HAPPY)
    music.play_melody("B A G F G A B C5 ", 500)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_icon(IconNames.SAD)
    for index in range(2):
        music.play_melody("E E E - C C C C ", 500)
input.on_button_pressed(Button.B, on_button_pressed_b)

walk_back_time = 0
shook_event = 0
basic.show_icon(IconNames.HEART)
music.play_melody("G B A G C5 B A B ", 448)

def on_forever():
    global shook_event, walk_back_time
    if input.magnetic_force(Dimension.STRENGTH) > 50:
        music.play_melody("E E E - C C C C ", 500)
        basic.show_icon(IconNames.NO)
        basic.pause(100)
        shook_event = 1
        walk_back_time = control.millis()
        TobbieII.shake_head(5)
        basic.pause(2000)
        TobbieII.backward()
        basic.pause(2000)
        while shook_event == 1:
            if control.millis() - walk_back_time > 8000:
                shook_event = 0
                TobbieII.stopwalk()
                basic.show_string("Magnet")
    if TobbieII.rblock(512):
        basic.show_leds("""
            . . # . .
                        . . . # .
                        # # # # #
                        . . . # .
                        . . # . .
        """)
        TobbieII.rightward()
        TobbieII.stopturn()
        basic.show_icon(IconNames.HAPPY)
    if TobbieII.lblock(512):
        basic.show_leds("""
            . . # . .
                        . # . . .
                        # # # # #
                        . # . . .
                        . . # . .
        """)
        TobbieII.leftward()
        TobbieII.stopturn()
        basic.show_icon(IconNames.HAPPY)
basic.forever(on_forever)
