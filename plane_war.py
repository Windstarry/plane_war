import pygame
import sys
from pygame.sprite import Group
from settings import Settings
from backgroud import BackGround
from ship import Ship
from bullet import Bullet
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    bg1 = BackGround(1,ai_settings,screen)
    bg2 = BackGround(2,ai_settings,screen)
    ship = Ship(ai_settings,screen)
    bullets = Group()
    pygame.display.set_caption("飞机大战")
    
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        bg1.update()
        bg2.update()
        bullets.update()
        gf.update_screen(bg1,bg2,ship,bullets)


if __name__ == "__main__":
    run_game()