import pygame
from pygame.sprite import Sprite

class Bullet( Sprite): 
    """ A class to manage pew-pews fired from the ship. very scary. much pew. """ 
    def __init__(self, ai_settings, screen, ship): 
        super().__init__() 
        self.screen = screen 
        self.rect = pygame.Rect( 0, 0, ai_settings.bullet_width, ai_settings.bullet_height) 
        self.rect.centerx = ship.rect.centerx #set bullet to ship's center
        self.rect.top = ship.rect.top #set bullet to top of ship
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color 
        self.speed_factor = ai_settings.bullet_speed_factor
    
    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect( self.screen, self.color, self.rect)

