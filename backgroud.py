import pygame

class BackGround(object):
    
    def __init__(self,num,ai_settings,screen):
        self.num = num
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load(ai_settings.bg_image)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect_start_settings()
        
    def rect_start_settings(self):
        if self.num == 1:
            self.rect.bottom = self.screen_rect.top
        else:
            self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        self.rect.centery += 1
        if self.rect.top == self.screen_rect.bottom:
            self.rect.bottom = self.screen_rect.top