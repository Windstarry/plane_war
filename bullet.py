import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self,ai_settings,screen,ship):
        #在飞船所处位置创建子弹位置
        super(Bullet,self).__init__()
        self.screen=screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load(self.ai_settings.bullet_image)
        self.rect = self.image.get_rect()
        #创建子弹，并设置子弹位置
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y=float(self.rect.y)
        #设置子弹速度
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        self.y -= self.speed_factor
        self.rect.y=self.y

    def blitme(self):
        self.screen.blit(self.image,self.rect)

