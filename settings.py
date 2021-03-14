class Settings():
    """Klasa przeznaczona do przechowywania wszystkich ustawień gry."""

    def __init__(self):
        """Inicjalizacja ustawień gry."""
        # Ustawienia ekranu.
        self.screen_width = 800
        self.screen_height = 600
        self.background_color = (230, 230, 230)

        # Ustawienia dotyczące statku kosmicznego.
        self.ship_limit = 3

        # Ustawienia dotyczące pocisku.
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Ustawienia dotyczące obcego
        self.fleet_drop_speed = 10

        # Łatwa zmiana szybkości gry.
        self.speeup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Inicjalizacja ustawień, które ulegają zmianie w trakcie gry."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # Wartość fleet_direction wynosząca 1 oznacza prawo, natomiast -1 oznacza lewo.
        self.fleet_direction = 1

    def increase_speed(self):
        """Zmiana ustawień dotyczących szybkości."""
        self.ship_speed *= self.speeup_scale
        self.bullet_speed *= self.speeup_scale
        self.alien_speed *= self.speeup_scale
