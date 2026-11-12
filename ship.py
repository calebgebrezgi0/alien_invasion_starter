"""
Program Name: Alien Invasion - Track 1: Custom Mechanics
Author: Caleb Gebrezgi
Purpose: Defines the ship's movement.
Starter Code: https://github.com/calebgebrezgi0/alien_invasion_starter.git
Date: 11-11-2026
"""
import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal



class Ship:
    """The player's ship."""


    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal'):
        """Load the ship image and place the ship at bottom center."""
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.ship_w, self.settings.ship_h),
        )

        self.rect = self.image.get_rect()
        self._center_ship()
        self.moving_right = False
        self.moving_left = False
        self.arsenal = arsenal

    def _center_ship(self):
        """Place the ship at the bottom center of the screen."""
        self.rect.midbottom = self.boundaries.midbottom
        self.x = float(self.rect.x)

    def update(self):
        """Update the ship's position and its bullets."""
        # updating the position of the ship
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        """Move the ship left or right within the screen edges."""
        temp_speed = self.settings.ship_speed
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += temp_speed
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= temp_speed

        self.rect.x = self.x

    def draw(self):
        """Draw the bullets and the ship."""
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self):
        """Fire from the arsenal.

        Returns:
            bool: True if a bullet was fired.
        """
        return self.arsenal.fire_bullet()

    def check_collisions(self, other_group):
        """Check for a collision with a sprite group.

        Args:
            other_group: The sprite group to check against.

        Returns:
            bool: True if the ship hit something.
        """
        if pygame.sprite.spritecollideany(self, other_group):
            self._center_ship()
            return True
        return False