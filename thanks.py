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


BORDER = 20
FONTSCALE = 2
BACKGROUND_COLOR = 0xFADADD
FOREGROUND_COLOR = 0xAA0088
TEXT_COLOR = 0xFFFF00
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
my_palette[0] = BACKGROUND_COLOR
tile_grid = displayio.TileGrid(my_bitmap, pixel_shader = my_palette, x = 0, y = 0)
screen.append(tile_grid)
inner_bitmap = displayio.Bitmap(display.width - BORDER*2, display.height - BORDER*2, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = FOREGROUND_COLOR



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
crust5 = Rect(85, 32, 8, 60, fill = 0xD2B48C, outline = None, stroke = 0)
screen.append(crust5)
crust6 = Rect(100, 29, 8, 78, fill = 0xD2B48C, outline = None, stroke = 0)
screen.append(crust6)
crust7 = Rect(120, 29, 9, 78, fill = 0xD2B48C, outline = None, stroke = 0)
screen.append(crust7)
crust8 = Rect(140, 32, 8, 78, fill = 0xD2B48C, outline = None, stroke = 0)
screen.append(crust8)
