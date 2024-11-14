#importsss
import board
import displayio
import terminalio
import time
from adafruit_display_text import label
from adafruit_st7789 import ST7789
from adafruit_display_shapes.rect import Rect
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.roundrect import RoundRect
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line


#display content
background_color = 0xFADADD
displayio.release_displays()
spi = board.SPI()
tft_cs = board.D3
tft_dc = board.D4
dbus = displayio.FourWire(spi, command = tft_dc, chip_select = tft_cs)
display = ST7789(dbus, rotation = 270, width = 240, height = 135, rowstart = 40, colstart = 53)
screen = displayio.Group()
display.root_group = screen 
my_bitmap = displayio.Bitmap(240, 135, 1)
my_palette = displayio.Palette(1)
my_palette[0] = background_color
tile_grid = displayio.TileGrid(my_bitmap, pixel_shader = my_palette, x = 0, y = 0)
screen.append(tile_grid)

# parts of my pie!!!
pieCrust = Circle(120, 67, 50, fill = 0x7B68EE, outline = 0xD2B48C, stroke = 12)
screen.append(pieCrust)

#horizontal crust
crust1 = Rect(80, 36, 78, 8, fill = 0xD2B48C, outline = None, stroke = 0)
screen.append(crust1)
crust2 = Rect(80, 54, 79, 8, fill = 0xD2B48C, outline = None, stroke = 0)
screen.append(crust2)
crust3 = Rect(80, 72, 79, 8, fill = 0xD2B48C, outline = None, stroke = 0)
screen.append(crust3)
crust4 = Rect(80, 90, 78, 8, fill = 0xD2B48C, outline = None, stroke = 0)
screen.append(crust4)

#vertical crust
crust5 = Rect(88, 32, 8, 60, fill = 0xD2B48C, outline = None, stroke = 0)
screen.append(crust5)
crust6 = Rect(106, 29, 8, 78, fill = 0xD2B48C, outline = None, stroke = 0)
screen.append(crust6)
crust7 = Rect(124, 29, 9, 78, fill = 0xD2B48C, outline = None, stroke = 0)
screen.append(crust7)
crust8 = Rect(142, 32, 8, 78, fill = 0xD2B48C, outline = None, stroke = 0)
screen.append(crust8)

#oven
oven = Rect(178, 8, 80, 135, fill = 0x3C4142, outline = None, stroke = 0)
screen.append(oven)
inside_oven = Rect(185, 80, 60, 30, fill = 0x000000, outline = None, stroke = 0)
screen.append(inside_oven)
oventop = Circle(220, 71, 35, fill = 0x000000, outline = None, stroke = 12)
screen.append(oventop)
#wordss
pieW = "pie!"
text_color = 0x800000
FONTSCALE = 2
text_area = label.Label(terminalio.FONT, text=pieW, color=text_color)
text_width = text_area.bounding_box[2] * FONTSCALE
text_group = displayio.Group(scale=FONTSCALE, x=19, y=92)
text_group.append(text_area)  
screen.append(text_group)
yumW = "yummm"
text_area2 = label.Label(terminalio.FONT, text=yumW, color=text_color)
text_width2 = text_area2.bounding_box[2] * FONTSCALE
text_group2 = displayio.Group(scale=FONTSCALE, x=19, y=111)
text_group2.append(text_area2)  
screen.append(text_group2)

#variables and whatnot
direction_x = 1
velocity_x = 6
direction_xC = 1
velocity_xC = 6
hcrustss = [crust1, crust2, crust3, crust4]
vcrustss = [ crust5, crust6, crust7, crust8]
#1C084A indgo dark
#main
while True:
    if pieCrust.x >= 175 or pieCrust.x <= 0:
        direction_x *= -1
    pieCrust.x += (velocity_x * direction_x)
    if pieCrust.x <= 0:
        pieCrust.fill = 0x7B68EE
        pieCrust.outline = 0xD2B48C
        for item in hcrustss:
            item.fill = 0xD2B48C
        for item in vcrustss:
            item.fill = 0xD2B48C
    if pieCrust.x >= 175:
        pieCrust.fill = 0x3F54BE
        pieCrust.outline = 0xC59260
        for item in hcrustss:
            item.fill = 0xC59260
        for item in vcrustss:
            item.fill = 0xC59260
    time.sleep(.02)
    for item in hcrustss:
        if item.x >= 81 or item.x <= 0:
            direction_xC *= -1
        item.x += (velocity_x * direction_x)
    time.sleep(.02)
    for item in vcrustss:
        if item.x >= 89 or item.x <= 0:
            direction_xC *= -1
        item.x += (velocity_x * direction_x)
    time.sleep(.02)
#importsss
import board
import displayio
import terminalio
import time
from adafruit_display_text import label
from adafruit_st7789 import ST7789
from adafruit_display_shapes.rect import Rect
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.roundrect import RoundRect
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line


#display content
background_color = 0xFADADD
displayio.release_displays()
spi = board.SPI()
tft_cs = board.D3
tft_dc = board.D4
dbus = displayio.FourWire(spi, command = tft_dc, chip_select = tft_cs)
display = ST7789(dbus, rotation = 270, width = 240, height = 135, rowstart = 40, colstart = 53)
screen = displayio.Group()
display.root_group = screen 
my_bitmap = displayio.Bitmap(240, 135, 1)
my_palette = displayio.Palette(1)
my_palette[0] = background_color
tile_grid = displayio.TileGrid(my_bitmap, pixel_shader = my_palette, x = 0, y = 0)
screen.append(tile_grid)

# parts of my pie!!!
pieCrust = Circle(120, 67, 50, fill = 0x7B68EE, outline = 0xD2B48C, stroke = 12)
screen.append(pieCrust)

#horizontal crust
crust1 = Rect(80, 36, 78, 8, fill = 0xD2B48C, outline = None, stroke = 0)
screen.append(crust1)
crust2 = Rect(80, 54, 79, 8, fill = 0xD2B48C, outline = None, stroke = 0)
screen.append(crust2)
crust3 = Rect(80, 72, 79, 8, fill = 0xD2B48C, outline = None, stroke = 0)
screen.append(crust3)
crust4 = Rect(80, 90, 78, 8, fill = 0xD2B48C, outline = None, stroke = 0)
screen.append(crust4)

#vertical crust
crust5 = Rect(88, 32, 8, 60, fill = 0xD2B48C, outline = None, stroke = 0)
screen.append(crust5)
crust6 = Rect(106, 29, 8, 78, fill = 0xD2B48C, outline = None, stroke = 0)
screen.append(crust6)
crust7 = Rect(124, 29, 9, 78, fill = 0xD2B48C, outline = None, stroke = 0)
screen.append(crust7)
crust8 = Rect(142, 32, 8, 78, fill = 0xD2B48C, outline = None, stroke = 0)
screen.append(crust8)

#oven
oven = Rect(178, 8, 80, 135, fill = 0x3C4142, outline = None, stroke = 0)
screen.append(oven)
inside_oven = Rect(185, 80, 60, 30, fill = 0x000000, outline = None, stroke = 0)
screen.append(inside_oven)
oventop = Circle(220, 71, 35, fill = 0x000000, outline = None, stroke = 12)
screen.append(oventop)
#wordss
pieW = "pie!"
text_color = 0x800000
FONTSCALE = 2
text_area = label.Label(terminalio.FONT, text=pieW, color=text_color)
text_width = text_area.bounding_box[2] * FONTSCALE
text_group = displayio.Group(scale=FONTSCALE, x=19, y=92)
text_group.append(text_area)  
screen.append(text_group)
yumW = "yummm"
text_area2 = label.Label(terminalio.FONT, text=yumW, color=text_color)
text_width2 = text_area2.bounding_box[2] * FONTSCALE
text_group2 = displayio.Group(scale=FONTSCALE, x=19, y=111)
text_group2.append(text_area2)  
screen.append(text_group2)

#variables and whatnot
direction_x = 1
velocity_x = 6
direction_xC = 1
velocity_xC = 6
hcrustss = [crust1, crust2, crust3, crust4]
vcrustss = [ crust5, crust6, crust7, crust8]
#1C084A indgo dark
#main
while True:
    if pieCrust.x >= 175 or pieCrust.x <= 0:
        direction_x *= -1
    pieCrust.x += (velocity_x * direction_x)
    if pieCrust.x <= 0:
        pieCrust.fill = 0x7B68EE
        pieCrust.outline = 0xD2B48C
        for item in hcrustss:
            item.fill = 0xD2B48C
        for item in vcrustss:
            item.fill = 0xD2B48C
    if pieCrust.x >= 175:
        pieCrust.fill = 0x3F54BE
        pieCrust.outline = 0xC59260
        for item in hcrustss:
            item.fill = 0xC59260
        for item in vcrustss:
            item.fill = 0xC59260
    time.sleep(.02)
    for item in hcrustss:
        if item.x >= 81 or item.x <= 0:
            direction_xC *= -1
        item.x += (velocity_x * direction_x)
    time.sleep(.02)
    for item in vcrustss:
        if item.x >= 89 or item.x <= 0:
            direction_xC *= -1
        item.x += (velocity_x * direction_x)
    time.sleep(.02)
