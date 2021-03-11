import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Klasa przedstawiająca pojedynczego obcego we flocie."""

    def __init__(self, alien_invasion_game):
        """Inicjalizacja obcego i zdefiniowanie jego położenia początkowego."""
        super().__init__()
        self.screen = alien_invasion_game.screen
        self.settings = alien_invasion_game.settings

        # Wczytanie obrazu obcego i zdefiniowanie jego atrybutu rect.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Umieszczenie nowego obcego w pobliżu lewego górnego rogu ekranu.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Przechowywanie dokładnego poziomu położenia obcego.
        self.alien_x = float(self.rect.x)

    def check_edges(self):
        """Zwraca wartość True, jeśli obcy znajduje się przy krawędzi ekranu."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self, *args, **kwargs):
        """Przesunięcie obcego w prawo lub w lewo."""
        self.alien_x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.alien_x
