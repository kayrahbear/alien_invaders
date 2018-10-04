import sys
import pygame

from bullet import Bullet

def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_pew = Bullet(ai_settings,screen,ship)
        bullets.add(new_pew)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)



def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """ 
    Responds to key presses in the game
    """
    for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events( event, ai_settings, screen, ship, bullets)
            elif event.type == pygame.KEYUP:
                check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, bullets):
    """
    update images on screen every loop
    """
    screen.fill(ai_settings.bg_color)

    for bullet in bullets.sprites(): 
        bullet.draw_bullet()
    ship.blitme()
        
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()

    for bullet in bullets.copy(): # kill the bullets that aren't showing on the screen anymore! 
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet) 
        
