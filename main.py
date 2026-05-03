def on_button_pressed_a():
    basic.show_icon(IconNames.HEART)
    mp3Player.play_file_in_time(1, 15)
input.on_button_pressed(Button.A, on_button_pressed_a)

# Bấm B để next bài khác

def on_button_pressed_b():
    basic.show_arrow(ArrowNames.EAST)
    mp3Player.play_in_time(mp3Player.PlayWhat.NEXT, 15)
input.on_button_pressed(Button.B, on_button_pressed_b)

# Bấm P1 để lùi bài phía trước

def on_pin_pressed_p1():
    basic.show_arrow(ArrowNames.WEST)
    mp3Player.play_in_time(mp3Player.PlayWhat.PREVIOUS, 15)
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

# +/ Format thẻ nhớ thành FAT32
# +/ Tạo thư mục: "mp3"
# +/ Đặt Tên file "xxxx_ABCD" (XXXX = 0001 --> 9999)
mp3Player.set_volume(20)
mp3Player.set_eq(mp3Player.EQ.NORMAL)