import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion():
    """Ogólna klasa przeznaczona do zarządzania zasobami i
    sposobem działania gry."""

    def __init__(self):
        """Inicjalizacja gry i utworzenie jej zasobów."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Inwazja obcych")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Rozpoczęcie pętli głównej gry."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        """Reakcja na zdarzenia generowane przez klawiaturę i mysz."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Reakcja na naciśnięcie klawisza."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Reakcja na zwolnienie klawisza."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Utworzenie nowego pocisku i dodanie go do grupy pocisków."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Uaktualnienie położenia pocisków i usunięcie tych niewidocznych
        na ekranie."""
        # Uaktualnienie położenia pocisków.
        self.bullets.update()

        # Usinięcie pocisków, które znajdują się poza ekraniem.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        """Utworzenie pełnej floty obcych."""
        # Utworzenie obcego i ustalenie liczby obcych, którzy zmieszczą się w rzędzie.
        # Odległość między poszczególnymi obcymi jest równa szerokości obcego.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Ustalenie, ile rzędów obcych zmieści się na ekranie.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Utworzenie pełnej floty obcych.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Utworzenie obcego i umieszczenie go w rzędzie."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.alien_x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.alien_x
        alien.rect.y = alien_height + 2 * alien_height * row_number
        self.aliens.add(alien)

    def _update_screen(self):
        """Uaktualnienie obrazów na ekranie i przejście do nowego ekranu."""
        self.screen.fill(self.settings.background_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Wyświetlenie ostatnio zmodyfikowanego ekranu.
        pygame.display.flip()

if __name__ == '__main__':
    # Utworzenie egzemplarza gry i jej uruchomienie.
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()
