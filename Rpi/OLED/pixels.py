from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106
import time

serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, rotate=0)

# Box and text rendered in portrait mode
with canvas(device) as draw:
    draw.point((5,9),fill=255)
    draw.point((6,9),fill=255)
    draw.point((7,9),fill=255)
    draw.point((8,9),fill=255)
    draw.point((9,9),fill=255)
while 1:
    time.sleep(1)
