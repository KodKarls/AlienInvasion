import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Klasa przeznaczona do zarządzania statkiem kosmicznym."""

    def __init__(self, alien_invasion_game):
        """Inicjalizacja statku kosmicznego i jego położenie początkowe."""
        super().__init__()
        self.screen = alien_invasion_game.screen
        self.setting = alien_invasion_game.settings
        self.screen_rect = alien_invasion_game.screen.get_rect()

        # Wczytanie obrazu statku kosmicznego i pobranie jego prostokąta.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Każdy nowy statek kosmiczny pojawia się na dole ekranu.
        self.rect.midbottom = self.screen_rect.midbottom

        # Położenie poziome statku jest przechowywane w postaci liczby zmiennoprzecinkowej.
        self.ship_x= float(self.rect.x)

        # Opcje wskazujące na poruszanie się statku.
        self.moving_right = False
        self.moving_left = False

    def update(self, *args, **kwargs):
        """Uaktualnienie położenia statku na podstawie opcji wskazującejna
        na jego ruch."""
        # Uaktuanienie wartości współrzędnej X statku, a nie jego prostokąta.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.ship_x += self.setting.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.ship_x -= self.setting.ship_speed

        # Uaktualnienie obiektu rect na podstawie wartości self.x.
        self.rect.x = self.ship_x

    def blitme(self):
        """Wyświetlenie statku kosmicznego w jego aktualnym położeniu."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Umieszczenie statku na środku przy dolnej krawędzi ekranu."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.ship_x = float(self.rect.x)
