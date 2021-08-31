# Hex_Demo
# Code that creates instance of a hex
import pygame
import math
import time
import random
from hex import Hex
from buttons import Button


DISPLAY_WIDTH = 1000
DISPLAY_HEIGHT = 1000

WHITE   =   (255,255,255)
BLACK   =   (0,0,0)
RED     =   (255,0,0)
LIME    =   (0,255,0)
BLUE    =   (0,0,255)
YELLOW  =   (255,255,0)
CYAN    =   (0,255,255)
MAGENTA =   (255,0,255)
SILVER  =   (192,192,192)
GRAY    =   (128,128,128)
MAROON  =   (128,0,0)
OLIVE   =   (128,128,0)
GREEN   =   (0,128,0)
PURPLE  =   (128,0,128)
TEAL    =   (0,128,128)
NAVY    =   (0,0,128)




TITLE = "Hexbusters" #Title for window frame
window = pygame.display.set_mode((DISPLAY_HEIGHT,DISPLAY_HEIGHT)) #dimensions of game screen
window.fill(WHITE)#background colour for game screen
pygame.display.update() #updates / applies the window parameters to the screen
pygame.display.set_caption(TITLE)




##hexagon parameters
Side_Length = 75
x = 200 #x-coordinate of first hex
y = 200 #y-coordinate of first hex
Seg_Height = math.sqrt((Side_Length**2)- ((0.5*Side_Length)**2)) #Pythag for distance from centre to mid of hex side
Colour = GRAY #Hes start colour
text = " " #text parameter default is empty until changed


###random letter selector snippet
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def letter():
    letter = alphabet[random.randint(0,25)]
    return letter


#####loads the start button image
#start_button_img = pygame.image.load('Start_Button.png').convert_alpha() #Loads Start button image file into Pygame



######Create Start Button Instance
#start_button = Button(850,10,start_button_img,0.15) #see "buttons module" method that blits this instance




window.fill(WHITE)

#########################1st Column##################################
###instances of the hexes that need drawing...using the hex module
hex1 = Hex(x, y+(Seg_Height*0), Side_Length,Colour, text = letter(), hexname='hex1') #Parameters for hex1 attributes
hex1.get_Hex_letter()#retrieves letter from hex object
hex1.get_Hex_letter_rectangle()#retrieves rectangle coordinates from letter render
hex2 = Hex(x,y+(Seg_Height*2),Side_Length,Colour, text = letter(), hexname='hex2')
hex2.get_Hex_letter()
hex2.get_Hex_letter_rectangle()
hex3 = Hex(x,y+(Seg_Height*4),Side_Length,Colour, text = letter(), hexname='hex3')
hex4 = Hex(x,y+(Seg_Height*6),Side_Length,Colour, text = letter(), hexname='hex4')

###########################2nd Column#################################
hex5 = Hex(x+(Side_Length*1.5) , y+Seg_Height, Side_Length,Colour, text = letter(), hexname='hex5' )
hex6 = Hex(x+(Side_Length*1.5) , y+(Seg_Height*3), Side_Length,Colour, text = letter(), hexname='hex6' )
hex7 = Hex(x+(Side_Length*1.5) , y+(Seg_Height*5), Side_Length,Colour, text = letter(), hexname='hex7')
hex8 = Hex(x+(Side_Length*1.5) , y+(Seg_Height*7), Side_Length,Colour, text = letter(), hexname='hex8' )

############################3rd Column################################
hex9 = Hex(x+(Side_Length*3) , y, Side_Length,Colour, text = letter(), hexname='hex9' )
hex10 = Hex(x+(Side_Length*3) , y+(Seg_Height*2), Side_Length,Colour, text = letter(), hexname='hex10')
hex11 = Hex(x+(Side_Length*3) , y+(Seg_Height*4), Side_Length,Colour, text = letter(), hexname='hex11')
hex12 = Hex(x+(Side_Length*3) , y+(Seg_Height*6), Side_Length,Colour, text = letter(), hexname='hex12')
#############################4th Column###############################
hex13 = Hex(x+(Side_Length*4.5) , y+Seg_Height, Side_Length,Colour, text = letter(), hexname='hex13')
hex14 = Hex(x+(Side_Length*4.5) , y+(Seg_Height*3), Side_Length,Colour, text = letter(), hexname='hex14')
hex15 = Hex(x+(Side_Length*4.5) , y+(Seg_Height*5), Side_Length,Colour, text = letter(), hexname='hex15')
hex16 = Hex(x+(Side_Length*4.5) , y+(Seg_Height*7), Side_Length, Colour, text = letter(), hexname='hex16')
##############################5th Column##############################
hex17 = Hex(x+(Side_Length*6) , y, Side_Length,Colour, text = letter(), hexname='hex17')
hex18 = Hex(x+(Side_Length*6) , y+(Seg_Height*2), Side_Length,Colour, text = letter(), hexname='hex18')
hex19 = Hex(x+(Side_Length*6) , y+(Seg_Height*4), Side_Length,Colour, text = letter(), hexname='hex19')
hex20 = Hex(x+(Side_Length*6) , y+(Seg_Height*6), Side_Length,Colour, text = letter(), hexname='hex20')
#################################################################
#########################Left Border Hexes#######################
hex21 =  Hex(x-(Side_Length*1.5) , y-Seg_Height, Side_Length,Colour=RED, text = "", hexname='hex21'   )
hex22 =  Hex(x-(Side_Length*1.5) , y+Seg_Height, Side_Length,Colour=RED, text = "" , hexname='hex22'  )
hex23 =  Hex(x-(Side_Length*1.5) , y+Seg_Height*3, Side_Length,Colour=RED, text = "", hexname='hex23' )
hex24 =  Hex(x-(Side_Length*1.5) , y+Seg_Height*5, Side_Length,Colour=RED, text = "", hexname='hex24' )
hex25 =  Hex(x-(Side_Length*1.5) , y+Seg_Height*7, Side_Length,Colour=RED, text = "", hexname='hex25' )

##################################################################
#########################Right Border Hexes#######################
hex26 =  Hex(x+(Side_Length*7.5) , y-Seg_Height, Side_Length,Colour=RED, text = "", hexname='hex26' )
hex27 =  Hex(x+(Side_Length*7.5) , y+Seg_Height, Side_Length,Colour=RED, text = "", hexname='hex27' )
hex28 =  Hex(x+(Side_Length*7.5) , y+Seg_Height*3, Side_Length,Colour=RED, text = "", hexname='hex28' )
hex29 =  Hex(x+(Side_Length*7.5) , y+Seg_Height*5, Side_Length,Colour=RED, text = "", hexname='hex29' )
hex30 =  Hex(x+(Side_Length*7.5) , y+Seg_Height*7, Side_Length,Colour=RED, text = "", hexname='hex30' )
hex31 =  Hex(x+(Side_Length*7.5) , y+Seg_Height, Side_Length,Colour=RED, text = "", hexname='hex31' )

##################################################################
#########################Top Border Hexes#######################
hex32 =  Hex(x , y-(Seg_Height*2), Side_Length,Colour=WHITE, text = "", hexname='hex32' )
hex33 =  Hex(x+(Side_Length*1.5) , y-Seg_Height, Side_Length,Colour=WHITE, text = "", hexname='hex33' )
hex34 =  Hex(x+(Side_Length*3) , y-Seg_Height*2, Side_Length,Colour=WHITE, text = "", hexname='hex34' )
hex35 =  Hex(x+(Side_Length*4.5) , y-Seg_Height, Side_Length,Colour=WHITE, text = "", hexname='hex35' )
hex36 =  Hex(x+(Side_Length*6) , y-Seg_Height*2, Side_Length,Colour=WHITE, text = "", hexname='hex36' )
hex37 =  Hex(x+(Side_Length*7.5) , y+Seg_Height, Side_Length,Colour=RED,   text = "", hexname='hex37' )



#################################################################
#########################Bottom Border Hexes#####################
hex38 =  Hex(x , y+(Seg_Height*8), Side_Length,Colour=WHITE, text = "", hexname='hex38' )
hex39 =  Hex(x+(Side_Length*1.5) , y+Seg_Height*9, Side_Length,Colour=WHITE, text = "", hexname='hex39' )
hex40 =  Hex(x+(Side_Length*3) , y+Seg_Height*8, Side_Length,Colour=WHITE, text = "", hexname='hex40' )
hex41 =  Hex(x+(Side_Length*4.5) , y+Seg_Height*9, Side_Length,Colour=WHITE, text = " ", hexname='hex41')
hex42 =  Hex(x+(Side_Length*6) , y+Seg_Height*8, Side_Length,Colour=WHITE, text = "", hexname='hex24' )


    #################################################################




    ############################Game Loop Starts######################################
run = False


while not run:


    for event in pygame.event.get():
        #Calls draw method from Hex Class
        hex1.draw(window)
        hex2.draw(window)
        hex3.draw(window)
        hex4.draw(window)
        hex5.draw(window)
        hex6.draw(window)
        hex7.draw(window)
        hex8.draw(window)
        hex9.draw(window)
        hex10.draw(window)
        hex11.draw(window)
        hex12.draw(window)
        hex13.draw(window)
        hex14.draw(window)
        hex15.draw(window)
        hex16.draw(window)
        hex17.draw(window)
        hex18.draw(window)
        hex19.draw(window)
        hex20.draw(window)
        hex21.draw(window)
        hex22.draw(window)
        hex23.draw(window)
        hex24.draw(window)
        hex25.draw(window)
        hex26.draw(window)
        hex27.draw(window)
        hex28.draw(window)
        hex29.draw(window)
        hex30.draw(window)
        hex31.draw(window)
        hex32.draw(window)
        hex33.draw(window)
        hex34.draw(window)
        hex35.draw(window)
        hex36.draw(window)
        hex37.draw(window)
        hex38.draw(window)
        hex39.draw(window)
        hex40.draw(window)
        hex41.draw(window)
        hex42.draw(window)


        if event.type==pygame.QUIT:
            run = True


        #if start_button.draw(window) == True:
        #    print ("START")


    pygame.display.update()
pygame.quit()
