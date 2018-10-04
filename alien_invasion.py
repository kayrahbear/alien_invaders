import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():

    pygame.init()

    ai_settings = Settings()
    
    screen = pygame.display.set_mode(( ai_settings.screen_width, ai_settings.screen_height)) 
    pygame.display.set_caption("Alien Invasion")

    pink_ship = Ship(ai_settings, screen)
    bullets = Group() # essentially an empty list that holds all the live bullets on the screen
    
    while True:
        gf.check_events(ai_settings, screen, pink_ship, bullets)
        pink_ship.update()
        gf.update_bullets(bullets)

        gf.update_screen(ai_settings,screen,pink_ship, bullets)


run_game()

