import time
import board
import neopixel

pixel = neopixel.NeoPixel(board.GP16, 1, brightness=1, auto_write=True)

def color_wheel(pos):
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

while True:
    for i in range(256):
        pixel[0] = color_wheel(i)
        time.sleep(0.1)