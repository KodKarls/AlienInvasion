class Settings:
    """A class to manage game settings."""

    def __init__(self):
        """Initialize Settings content."""

        # Screen settings.
        self.screen_width = 800
        self.screen_height = 600
        self.background_color = (230, 230, 230)

        # Font settings.
        self.font_name = 'Courier'
        self.font_point_size = 48
        self.font_button_size = 40

        # Ship settings.
        self.ship_limit = 3

        # Bullet settings.
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings.
        self.fleet_drop_speed = 10
        self.fleet_direction = 1       # (1) - moving right, (-1) moving left
        self.alien_points = 50

        # Dynamic settings.
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # Dynamic scale settings.
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.reset_dynamic_settings()

    def reset_dynamic_settings(self):
        """Reset dynamic settings."""

        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        """Increase dynamic settings with dynamic scale."""

        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
