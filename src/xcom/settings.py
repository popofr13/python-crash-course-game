class Settings:
    """A class to store all settings for Alien Invasions"""

    def __init__(self) -> None:
        """Initialize the game's settings."""
        # Ship settings
        self.ship_speed = 2.5

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

    def display_mode(self) -> tuple[int, int]:
        return (self.screen_width, self.screen_height)
