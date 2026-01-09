from typing import Self


class Alien:
    x: float = 0
    y: float = 0
    # valor por defecto
    level_health: int = 3
    counter_alien = 0

    def __init__(self, x: float, y: float, level_health: int = 3) -> None:
        """Represents an alien entity in the game.

            Keeps track of its position, health, and counts how many
        aliens have been created globally via a class variable.

        Attributes:
            counter_alien (int): Global counter of created Alien instances.
        """
        self.x = x
        self.y = y
        self.level_health = level_health
        Alien.counter_alien += 1

    def hit(self, level_damage: int = 1) -> None:
        """Applies damage to the Alien, reducing its health.

        Args:
            level_damage: Amount of damage to apply. Defaults to 1.
        """
        self.level_health -= level_damage

    def is_alive(self) -> bool:
        """Checks if the Alien is still alive.

        Returns:
            True if health is greater than 0, False otherwise.
        """
        return self.level_health > 0

    def teleport(self, x_tp: float, y_tp: float) -> None:
        """Teleports the Alien to a new position instantly.

        Args:
            x_tp: New X coordinate.
            y_tp: New Y coordinate.
        """
        self.x = x_tp
        self.y = y_tp

    def collision(self, object_coll: Self) -> bool:
        """Detects if this Alien collides with another Alien.

        Compares the exact coordinates of both objects.

        Args:
            object_coll: Another instance of the Alien class (Self).

        Returns:
            True if coordinates (x, y) are identical.
        """
        if self.x == object_coll.x and self.y == object_coll.y:
            return True

        return False


def new_aliens_collection(start_positions: list[tuple[int, int]]) -> list[Alien]:
    """Creates a fleet of aliens from a list of coordinates.
    
    Args:
        start_positions: List of tuples (x, y) containing initial positions.
                        Example: [(0, 0), (5.5, 10.2)]
    
    Returns:
        A list containing the created Alien objects.
    """
    return [Alien(x, y) for x, y in start_positions]


if __name__ == "__main__":
    alien_nicki = Alien(5, 6)
    aliens = new_aliens_collection([(4, 7), (-1, 0)])
    for alien in aliens:
        print(alien.x, alien.y)
