# Hexbuster Hex Class
import math
import pygame


class Hex():
    shape = "Hex"

    def __init__(self, x,y, Side_Length,Colour, text):
            self.text = text
            self.font = pygame.font.Font("arial_copy.ttf",20)
            self.letter = self.font.render(self.text, True, (0,0,0))
            self.Side_Length    = Side_Length
            self.Centre_pt_x    = x
            self.Centre_pt_y    = y
            self.Seg_Height     = math.sqrt((self.Side_Length**2)- ((0.5*self.Side_Length)**2))
            self.color          = Colour
            self.Vertices_1     = (self.Centre_pt_x - (0.5*self.Side_Length), self.Centre_pt_y-self.Seg_Height)
            self.Vertices_2     = (self.Centre_pt_x + (0.5*self.Side_Length), self.Centre_pt_y-self.Seg_Height)
            self.Vertices_3     = (self.Centre_pt_x +  self.Side_Length     , self.Centre_pt_y)
            self.Vertices_4     = (self.Centre_pt_x + (0.5*self.Side_Length), self.Centre_pt_y+self.Seg_Height)
            self.Vertices_5     = (self.Centre_pt_x - (0.5*self.Side_Length), self.Centre_pt_y+self.Seg_Height)
            self.Vertices_6     = (self.Centre_pt_x -  self.Side_Length     , self.Centre_pt_y)
            self.clicked        = False
            #self.letterbox_width = self.letter.get_width()
            #self.letterbox_height = self.letter.get_height()
            self.letterbox_rect = self.letter.get_rect()
            #print("letterbox rectangle = " ,self.letterbox_rect)


            self.WHITE   =   (255,255,255)
            self.BLACK   =   (0,0,0)
            self.RED     =   (255,0,0)
            self.LIME    =   (0,255,0)
            self.BLUE    =   (0,0,255)
            self.YELLOW  =   (255,255,0)
            self.CYAN    =   (0,255,255)
            self.MAGENTA =   (255,0,255)
            self.SILVER  =   (192,192,192)
            self.GRAY    =   (128,128,128)
            self.MAROON  =   (128,0,0)
            self.OLIVE   =   (128,128,0)
            self.GREEN   =   (0,128,0)
            self.PURPLE  =   (128,0,128)
            self.TEAL    =   (0,128,128)
            self.NAVY    =   (0,0,128)





    def draw(self, window):
        pygame.draw.polygon(window, self.color, [self.Vertices_1,self.Vertices_2,self.Vertices_3, self.Vertices_4, self.Vertices_5, self.Vertices_6])
        pygame.draw.polygon(window, self.BLACK, [self.Vertices_1,self.Vertices_2,self.Vertices_3, self.Vertices_4, self.Vertices_5, self.Vertices_6],1)
        window.blit(self.letter,(self.Centre_pt_x-5,self.Centre_pt_y-10))

        #getmouse position
        hex_mouse_pos = pygame.mouse.get_pos()
        print("Hex_mouse Pos = ", hex_mouse_pos)
        if self.letterbox_rect.collidepoint(hex_mouse_pos):
            print("Hex found")




    def get_Hex_letter(self):
        print("Hex Letter Getter activated...", self.text)
        return self.text

    def get_Hex_letter_rectangle(self):
        print("Rendering rectangle behind letter",self.text, " is..", self.letterbox_rect)
        return self.letterbox_rect



