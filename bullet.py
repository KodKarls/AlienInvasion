import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Klasa przeznaczona do zarządzania pociskami wystrzeliwanymi
    przez statek."""

    def __init__(self, alien_invasion_game):
        """Utworzenie obiektu pocisku w aktualnym położeniu statku."""
        super().__init__()
        self.screen = alien_invasion_game.screen
        self.settings = alien_invasion_game.settings
        self.color = self.settings.bullet_color

        # Utworzenie prostokąta pocisku w punkcie (0, 0), a następnie
        # zdefiniowanie dla niego odpowidniego położenia
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = alien_invasion_game.ship.rect.midtop

        # Położenie pocisku jest zdefiniowane za pomocą wartości zmiennoprzecinkowej
        self.bullet_y = float(self.rect.y)

    def update(self, *args, **kwargs):
        """Poruszanie pociskiem po ekranie."""
        # Uaktualnienie położenia pocisku.
        self.bullet_y -= self.settings.bullet_speed
        # Uaktualnienie położenia prostokąta pocisku.
        self.rect.y = self.bullet_y

    def draw_bullet(self):
        """Wyświetlanie pocisku na ekranie."""
        pygame.draw.rect(self.screen, self.color, self.rect)
