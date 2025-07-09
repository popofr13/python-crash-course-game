# region Circular imports fix
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
# endregion

import pygame

class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_agame: AlienInvasion):
        """Initialize the ship and set its starting position"""
        self.screen = ai_agame.screen
        self.screen_rect = ai_agame.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)