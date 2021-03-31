import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self,ai_settings,screen):
        super(Alien,self).__init__()
        self.screen=screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load(self.ai_settings.alien_image)
        self.rect = self.image.get_rect()
        #设置飞船出现于屏幕左上方
        self.rect.x = self.rect.width
        self.rect.y = -self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        #设置敌机速度
        self.speed_factor = ai_settings.alien_speed_factor

    def update(self):
        self.y += self.speed_factor
        self.rect.y=self.y

    def blitme(self):
        self.screen.blit(self.image,self.rect)


      
