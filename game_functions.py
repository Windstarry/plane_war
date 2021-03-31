from bullet import Bullet
from alien import Alien
import sys
import pygame
from time import sleep
import random

def start_game(ai_settings,screen,stats,sb,ship,aliens,bullets):
    #飞船速度初始化
    ai_settings.initialize_dynamic_settings()
    pygame.mouse.set_visible(False)
    stats.reset_stats()
    stats.game_active = True
    sb.prep_score()
    sb.prep_high_score()
    sb.prep_level()
    sb.prep_ships()
    
    aliens.empty()
    bullets.empty()
    create_fleet(ai_settings,screen,stats,sb,ship,aliens,bullets)
    ship.center_ship()
     
def check_keydown_events(event,ai_settings,screen,stats,sb,ship,aliens,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right=True
    elif event.key == pygame.K_LEFT:
        ship.moving_left=True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_p and not stats.game_active:
        start_game(ai_settings,screen,stats,sb,ship,aliens,bullets)
    elif event.key == pygame.K_ESCAPE:
        stats. write_high_score(stats.high_score)
        sys.exit()

def fire_bullet(ai_settings,screen,ship,bullets):
    if len(bullets) < ai_settings.bullet_allowed:
            new_bullet = Bullet(ai_settings,screen,ship)
            bullets.add(new_bullet)

def create_alien(ai_settings,screen,aliens):
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    available_aliens_x = int(ai_settings.screen_width/alien_width)-1
    alien.x = alien_width*random.randint(1,available_aliens_x)
    alien.rect.x = alien.x
    aliens.add(alien)

def create_fleet(ai_settings,screen,stats,sb,ship,aliens,bullets):
    number_aliens_x = ai_settings.alien_allowed
    for alien_number in range(number_aliens_x):
        if len(aliens) < ai_settings.alien_allowed:
            create_alien(ai_settings,screen,aliens)
        
def check_aliens_rect(ai_settings,stats,screen,ship,aliens,bullets):
    for alien in aliens.copy():
        if (alien.rect.bottom >= ai_settings.screen_height 
                or alien.rect.right <= 0 
                or alien.rect.left >= ai_settings.screen_width):
            aliens.remove(alien)

def update_alien(ai_settings,screen,stats,sb,ship,aliens,bullets):
    aliens.update()
    check_aliens_rect(ai_settings,stats,screen,ship,aliens,bullets)
    if pygame.sprite.spritecollideany(ship,aliens):
        #print("飞船爆炸")
        ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)

def ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets):
    
    if stats.ships_left > 0:
        stats.ships_left -= 1
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings,screen,stats,sb,ship,aliens,bullets)
        ship.center_ship()
        sleep(1)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right=False
    elif event.key == pygame.K_LEFT:
        ship.moving_left=False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stats. write_high_score(stats.high_score)
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,stats,sb,ship,aliens,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button,mouse_x,mouse_y)

def check_play_button(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button,mouse_x,mouse_y):
    if play_button.rect.collidepoint(mouse_x,mouse_y) and not stats.game_active:
        start_game(ai_settings,screen,stats,sb,ship,aliens,bullets)

def update_screen(bg1,bg2,stats,sb,ship,aliens,bullets,play_button):
    bg1.blitme()
    bg2.blitme()
    ship.blitme()
    for bullet in bullets.sprites():
        bullet.blitme()
    for alien in aliens.sprites():
        alien.blitme()
    if not stats.game_active:
        play_button.draw_button()
    sb.show_score()
    pygame.display.flip()

def update_background(bg1,bg2):
    bg1.update()
    bg2.update()

def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets)

def check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets):
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points*len(aliens)
            sb.prep_score()
        check_high_score(stats,sb)
        check_level_up(ai_settings,stats,sb)

def check_high_score(stats,sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

def check_level_up(ai_settings,stats,sb):
    level = stats.score // 100
    if level > stats.level:
        ai_settings.increase_speed()
        stats.level += 1
        sb.prep_level()
        

