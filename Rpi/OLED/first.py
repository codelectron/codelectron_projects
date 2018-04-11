from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106
import time

serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, rotate=0)

# Box and text rendered in portrait mode
with canvas(device) as draw:
    draw.rectangle(device.bounding_box, outline="white", fill="black")
    draw.text((10, 40), "WWW.CODELECTRON.COM", fill="white")
while 1:
    time.sleep(1)
