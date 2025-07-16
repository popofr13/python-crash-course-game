from .alien_invasion import AlienInvasion


def main() -> None:
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
