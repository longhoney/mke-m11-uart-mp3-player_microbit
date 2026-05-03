input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Heart)
    mp3Player.playFileInTime(1, 15)
})
// Bấm B để next bài khác
input.onButtonPressed(Button.B, function () {
    basic.showArrow(ArrowNames.East)
    mp3Player.playInTime(mp3Player.PlayWhat.Next, 15)
})
// Bấm P1 để lùi bài phía trước
input.onPinPressed(TouchPin.P1, function () {
    basic.showArrow(ArrowNames.West)
    mp3Player.playInTime(mp3Player.PlayWhat.Previous, 15)
})
// +/ Format thẻ nhớ thành FAT32
// +/ Tạo thư mục: "mp3"
// +/ Đặt Tên file "xxxx_ABCD" (XXXX = 0001 --> 9999)
mp3Player.setVolume(20)
mp3Player.setEQ(mp3Player.EQ.Normal)
