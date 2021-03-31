import pygame
import sys
from pygame.sprite import Group
from settings import Settings
from backgroud import BackGround  
from ship import Ship
from bullet import Bullet
from alien import Alien
import game_functions as gf
from game_stats import GameStats
from scoreboard import ScoreBoard
from button import Button

def run_game():
    pygame.init()
    pygame.display.set_caption("飞机大战")
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    bg1 = BackGround(ai_settings,screen)
    bg2 = BackGround(ai_settings,screen,is_alt=True)
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    play_button = Button(ai_settings,screen,'Play')
    stats = GameStats(ai_settings)
    sb = ScoreBoard(ai_settings,screen,stats)
    
    while True:
        gf.check_events(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)
        if stats.game_active:
            gf.update_background(bg1,bg2)
            ship.update()
            gf.create_fleet(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_alien(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
             
        gf.update_screen(bg1,bg2,stats,sb,ship,aliens,bullets,play_button)


if __name__ == "__main__":
    run_game()  