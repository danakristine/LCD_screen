#importsss
import board
import displayio
import terminalio
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
pieCrust = Circle(120, 67, 50, fill = 0x703BE7, outline = 0xD2B48C, stroke = 12)
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

#main
while True:
    pass
