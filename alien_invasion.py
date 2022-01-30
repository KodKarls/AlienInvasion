import sys
from time import sleep

import pygame

from utils.settings import Settings
from utils.game_stats import GameStats
from utils.scoreboard import Scoreboard
from utils.file_manager import FileManager
from gui.button import Button
from entity.ship import Ship
from entity.bullet import Bullet
from entity.alien import Alien

class AlienInvasion:
    """A class designed to manage all resources and the working way of the game."""

    def __init__(self):
        """Initialize all game content."""

        pygame.init()
        self.settings = Settings()

        # Screen settings.
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Inwazja obcych")

        # Create game stats object and scoreboard object.
        self.stats = GameStats(self)
        self.scoreboard = Scoreboard(self)

        # Create entities.
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        # Create play button.
        self.play_button = Button(self, "Gra")

        # Create file manager.
        self.file_manager = FileManager()

    def run_game(self):
        """Run the main loop game."""

        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _check_events(self):
        """React to events triggered by the keyboard and mouse."""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the user clicks the Game button."""

        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset dynamic game settings.
            self.settings.reset_dynamic_settings()

            # Reset static game data.
            self.stats.reset_stats()
            self.stats.game_active = True
            self.scoreboard.prep_score()
            self.scoreboard.prep_level()
            self.scoreboard.prep_ships()

            # Remove contents from alien and bullet list.
            self.aliens.empty()
            self.bullets.empty()

            # Create the new aliens fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """React to press the key."""

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """React to release the key."""

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to bullet groups."""

        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update bullets position."""

        self.bullets.update()

        # Remove bullets, which are out of the screen.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """React for collision between a bullet and alien."""

        # Remove all bullets and aliens, which collide with each other .
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.scoreboard.prep_score()
            self.scoreboard.check_high_score()

        if not self.aliens:
            # Remove existing bullets, speed up the game and create a new alien fleet.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Update the game level.
            self.stats.level += 1
            self.scoreboard.prep_level()

    def _update_aliens(self):
        """Update aliens fleet position."""

        self._check_fleet_edges()
        self.aliens.update()

        # Detect collision between alien and ship.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Find aliens, which achieve the bottom edge of the screen.
        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        """Check if any alien rich the bottom edge of the screen."""

        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # The same as the case in collision alien with the ship.
                self._ship_hit()
                break

    def _ship_hit(self):
        """React for collision between the alien and the ship."""

        if self.stats.ships_left > 0:
            # Decrease player lives and update scoreboard.
            self.stats.ships_left -= 1
            self.scoreboard.prep_ships()

            # Remove contents from alien and bullet list.
            self.aliens.empty()
            self.bullets.empty()

            # Create the new aliens fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Pause a half second.
            sleep(0.5)
        else:
            self.file_manager.save_data(self.stats.score)
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _create_fleet(self):
        """Create aliens fleet."""

        # Create an alien and determine the number of aliens that will fit in a row. The distance between each alien is
        # equal to the width of the alien.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determine how many rows of aliens will fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Create a complete aliens fleet.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create the alien and place it in the row."""

        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.alien_x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.alien_x
        alien.rect.y = alien_height + 2 * alien_height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """React, when the alien rach the edge of the screen."""

        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Move all aliens fleet to the bottom and change its direction."""

        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """Update all images on the screen."""

        self.screen.fill(self.settings.background_color)
        self.ship.display()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Display all scoreboard data.
        self.scoreboard.show_data()

        # Display the play button, when the game is disabled.
        if not self.stats.game_active:
            self.play_button.draw_button()

        # Display the last modified screen.
        pygame.display.flip()


if __name__ == '__main__':
    # Create the instance of the game and run it.
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()
