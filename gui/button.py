import pygame.font

class Button:
    """A class to manage buttons."""

    def __init__(self, alien_invasion_game, width, height, pos_y, msg):
        """Initialize Button content."""

        self.screen = alien_invasion_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = alien_invasion_game.settings

        # Define the dimensions and properties of the button.
        self.width, self.height = width, height
        self.pos_y = pos_y
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(self.settings.font_name, self.settings.font_button_size)

        # Create a button rectangle and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery + 120 - self.pos_y

        # Prepare message - only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Place a message in the generated image and center the text on the button."""

        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Display the button and its text.

        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
