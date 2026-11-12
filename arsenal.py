"""
Program Name: Alien Invasion - Track 1: Custom Mechanics
Author: Caleb Gebrezgi
Purpose: Managing the ship's bullets.
Starter Code: https://github.com/calebgebrezgi0/alien_invasion_starter.git
Date: 11-11-2026
"""
import pygame
from bullet import Bullet
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    

class Arsenal:
    """Holds the bullets that are currently on screen."""

    def __init__(self, game: 'AlienInvasion'):
        """Create an empty bullet group."""
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self):
        """Move all bullets and remove the ones that left the screen."""
        self.arsenal.update()
        self._remove_bullets_off_screen()

    def _remove_bullets_off_screen(self):
        """Delete bullets that left the top of the screen."""
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)

    def draw(self):
        """Draw every bullet."""
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self):
        """Fire a bullet if the magazine isn't full.

        Returns:
            bool: True if a bullet was fired, False if the magazine is full.
        """
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False