import pygame
from pygame.sprite import Sprite
#When using sprites, you can group related elements in your game and act on all the grouped
#elements at once
class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen 
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #Create a bullet rect at (0, 0) (Top left of screen) and then set correct position.
        #setting the rect.midtop to be equal to ai_game.ship.rect.midtop will make the bullet
        #seem to emerge from the top of the ship, having been fired
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, 
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        #Update the decimal position of the bullet/
        self.y -= self.settings.bullet_speed
        #Update the rect position
        self.rect.y = self.y
    
    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)