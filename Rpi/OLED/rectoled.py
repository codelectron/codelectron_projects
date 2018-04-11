from PIL import ImageFont, ImageDraw
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106
import time

serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, rotate=0)

# Box and text rendered in portrait mode

with canvas(device) as draw:
    font = ImageFont.load_default()
    draw.rectangle((0, 0, 40, 40), outline=255, fill=255)
    draw.line((0,0 , 20 , 20 ), fill="white")

raw_input("Enter to exit")
