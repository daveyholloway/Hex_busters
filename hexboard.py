# Hex_Demo
# Code that creates instance of a hex
import pygame
import math
from hex import Hex






class HexBoard(Hex):
#hex2 = Hex()#need to change the position by passing through new (x,y) coordinates
    def __init__(self, x,y, Side_Length,Colour):
        shape = "board"


    def draw(x,y,Side_Length, Seg_Height, Colour):
        window.fill(WHITE)

        #########################1st Column##################################

        hex1 = Hex(x , y+(Seg_Height*0), Side_Length,Colour )
        hex1.draw(window)

        hex2 = Hex(x,y+(Seg_Height*2),Side_Length,Colour)
        hex2.draw(window)

        hex3 = Hex(x,y+(Seg_Height*4),Side_Length,Colour)
        hex3.draw(window)

        hex4 = Hex(x,y+(Seg_Height*6),Side_Length,Colour)
        hex4.draw(window)

        ###########################2nd Column#################################

        hex5 = Hex(x+(Side_Length*1.5) , y+Seg_Height, Side_Length,Colour )
        hex5.draw(window)

        hex6 = Hex(x+(Side_Length*1.5) , y+(Seg_Height*3), Side_Length,Colour )
        hex6.draw(window)

        hex7 = Hex(x+(Side_Length*1.5) , y+(Seg_Height*5), Side_Length,Colour)
        hex7.draw(window)

        hex8 = Hex(x+(Side_Length*1.5) , y+(Seg_Height*7), Side_Length,Colour )
        hex8.draw(window)

        ############################3rd Column################################

        hex9 = Hex(x+(Side_Length*3) , y, Side_Length,Colour )
        hex9.draw(window)

        hex10 = Hex(x+(Side_Length*3) , y+(Seg_Height*2), Side_Length,Colour)
        hex10.draw(window)

        hex11 = Hex(x+(Side_Length*3) , y+(Seg_Height*4), Side_Length,Colour)
        hex11.draw(window)

        hex12 = Hex(x+(Side_Length*3) , y+(Seg_Height*6), Side_Length,Colour)
        hex12.draw(window)

        #############################4th Column###############################

        hex13 = Hex(x+(Side_Length*4.5) , y+Seg_Height, Side_Length,Colour)
        hex13.draw(window)

        hex14 = Hex(x+(Side_Length*4.5) , y+(Seg_Height*3), Side_Length,Colour)
        hex14.draw(window)

        hex15 = Hex(x+(Side_Length*4.5) , y+(Seg_Height*5), Side_Length,Colour)
        hex15.draw(window)

        hex16 = Hex(x+(Side_Length*4.5) , y+(Seg_Height*7), Side_Length, Colour)
        hex16.draw(window)

        ##############################5th Column##############################

        hex17 = Hex(x+(Side_Length*6) , y, Side_Length,Colour)
        hex17.draw(window)

        hex18 = Hex(x+(Side_Length*6) , y+(Seg_Height*2), Side_Length,Colour)
        hex18.draw(window)

        hex19 = Hex(x+(Side_Length*6) , y+(Seg_Height*4), Side_Length,Colour)
        hex19.draw(window)

        hex20 = Hex(x+(Side_Length*6) , y+(Seg_Height*6), Side_Length,Colour)
        hex20.draw(window)

        #################################################################
        #########################Left Border Hexes#######################
        hex21 =  Hex(x-(Side_Length*1.5) , y-Seg_Height, Side_Length,Colour=RED )
        hex21.draw(window)

        hex22 =  Hex(x-(Side_Length*1.5) , y+Seg_Height, Side_Length,Colour=RED )
        hex22.draw(window)

        hex23 =  Hex(x-(Side_Length*1.5) , y+Seg_Height*3, Side_Length,Colour=RED )
        hex23.draw(window)

        hex24 =  Hex(x-(Side_Length*1.5) , y+Seg_Height*5, Side_Length,Colour=RED )
        hex24.draw(window)

        hex25 =  Hex(x-(Side_Length*1.5) , y+Seg_Height*7, Side_Length,Colour=RED )
        hex25.draw(window)


        ##################################################################
        #########################Right Border Hexes#######################
        hex26 =  Hex(x+(Side_Length*7.5) , y-Seg_Height, Side_Length,Colour=RED )
        hex26.draw(window)

        hex27 =  Hex(x+(Side_Length*7.5) , y+Seg_Height, Side_Length,Colour=RED )
        hex27.draw(window)

        hex28 =  Hex(x+(Side_Length*7.5) , y+Seg_Height*3, Side_Length,Colour=RED )
        hex28.draw(window)

        hex29 =  Hex(x+(Side_Length*7.5) , y+Seg_Height*5, Side_Length,Colour=RED )
        hex29.draw(window)

        hex30 =  Hex(x+(Side_Length*7.5) , y+Seg_Height*7, Side_Length,Colour=RED )
        hex30.draw(window)

        hex31 =  Hex(x+(Side_Length*7.5) , y+Seg_Height, Side_Length,Colour=RED )
        hex31.draw(window)

        ##################################################################
        #########################Top Border Hexes#######################
        hex32 =  Hex(x , y-(Seg_Height*2), Side_Length,Colour=WHITE )
        hex32.draw(window)

        hex33 =  Hex(x+(Side_Length*1.5) , y-Seg_Height, Side_Length,Colour=WHITE )
        hex33.draw(window)

        hex34 =  Hex(x+(Side_Length*3) , y-Seg_Height*2, Side_Length,Colour=WHITE )
        hex34.draw(window)

        hex35 =  Hex(x+(Side_Length*4.5) , y-Seg_Height, Side_Length,Colour=WHITE )
        hex35.draw(window)

        hex36 =  Hex(x+(Side_Length*6) , y-Seg_Height*2, Side_Length,Colour=WHITE )
        hex36.draw(window)

        hex37 =  Hex(x+(Side_Length*7.5) , y+Seg_Height, Side_Length,Colour=WHITE )
        hex31.draw(window)


        #################################################################
        #########################Bottom Border Hexes#####################
        hex38 =  Hex(x , y+(Seg_Height*8), Side_Length,Colour=WHITE )
        hex38.draw(window)

        hex39 =  Hex(x+(Side_Length*1.5) , y+Seg_Height*9, Side_Length,Colour=WHITE )
        hex39.draw(window)

        hex40 =  Hex(x+(Side_Length*3) , y+Seg_Height*8, Side_Length,Colour=WHITE )
        hex40.draw(window)

        hex41 =  Hex(x+(Side_Length*4.5) , y+Seg_Height*9, Side_Length,Colour=WHITE )
        hex41.draw(window)

        hex42 =  Hex(x+(Side_Length*6) , y+Seg_Height*8, Side_Length,Colour=WHITE )
        hex42.draw(window)

        #################################################################
