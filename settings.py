class Settings(): 
    def __init__( self): 
        self.screen_width = 1200 
        self.screen_height = 800 
        self.bg_color = (254,255,190)
        self.ship_speed_factor = 1.5

        self.bullet_speed_factor = 1
        self.bullet_width = 8
        self.bullet_height = 12
        self.bullet_color = (191,185,255)
        self.bullets_allowed = 3

        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # 1 for right, -1 for left


