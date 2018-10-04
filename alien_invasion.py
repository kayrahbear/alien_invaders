import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():

    pygame.init()

    ai_settings = Settings()
    
    screen = pygame.display.set_mode(( ai_settings.screen_width, ai_settings.screen_height)) 
    pygame.display.set_caption("Alien Invasion")

    pink_ship = Ship(ai_settings, screen)
    
    while True:
        gf.check_events(pink_ship)
        pink_ship.update_location()
        gf.update_screen(ai_settings,screen,pink_ship)


run_game()

