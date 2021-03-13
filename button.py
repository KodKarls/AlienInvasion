import pygame.font

class Button():
    """Klasa przedstawiająca pojedynczy przycisk w grze."""

    def __init__(self, alien_invasion_game, msg):
        """Inicjalizacja atrybutów przycisku."""
        self.screen = alien_invasion_game.screen
        self.screen_rect = self.screen.get_rect()

        # Zdefiniowanie wymiarów i właściwości przycisku.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_colot = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Utworzenie prostokąta przycisku i wyśrodkowanie go.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Komunikat wyświetlany przez przycisk trzeba przygotować tylko jednokrotnie.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Umieszczenie komunikatu w wygenerowanym obrazie i wyśrodkowanie tekstu na
        przycisku."""
        self.msg_image = self.font.render(msg, True, self.text_colot, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Wyświetlenie pustego przycisku, a następnie komunikatu na nim.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
