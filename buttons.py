# Button class
import pygame


class Button():
    def __init__(self, x, y, image, scale): #image parameters with sscale variable determining eventual size on screen
        width = image.get_width() #retrieves start button image width
        height = image.get_height() #retrieves start button image height

        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale))) #Transform original height and width with SCALE
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self,window):
        action = False
        pos = pygame.mouse.get_pos() #gets mouse position
        if self.rect.collidepoint(pos):
            print("HOVER")
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False




        window.blit(self.image, (self.rect.x, self.rect.y))######updates/Blits/Pastes Start Button Instance

        return action
