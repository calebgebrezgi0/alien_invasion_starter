"""
Program Name: Alien Invasion - Track 1: Custom Mechanics
Author: Caleb Gebrezgi
Purpose: Defines the Bullet sprite that the ship fires.
Starter Code: https://github.com/calebgebrezgi0/alien_invasion_starter.git
Date Updated: 11-11-2026
"""
import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
    """A bullet fired from the ship."""

    def __init__(self, game: 'AlienInvasion'):
        """Create a bullet at the ship's nose."""
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.bullet_w, self.settings.bullet_h)
        )


        self.rect = self.image.get_rect()
        self.rect.midtop = self.game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet on the screen."""
        self.screen.blit(self.image, self.rect)