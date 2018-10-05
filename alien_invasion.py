import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():

    pygame.init()

    ai_settings = Settings()
    
    screen = pygame.display.set_mode(( ai_settings.screen_width, 
    ai_settings.screen_height)) 
    pygame.display.set_caption("Alien Invasion")

    pink_ship = Ship(ai_settings, screen)
    bullets = Group() # essentially an empty list
    aliens = Group()

    gf.create_fleet(ai_settings,screen,pink_ship,aliens)

    while True:
        gf.check_events(ai_settings, screen, pink_ship, bullets)
        pink_ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(ai_settings, aliens)

        gf.update_screen(ai_settings,screen,pink_ship, aliens, bullets)


run_game()

