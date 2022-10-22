from game.casting.actor import Actor


class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self, player):
        super().__init__()
        self._points = 0
        self.add_points(0, player) #Added a player argument to the points in order to keep the code below simpler.

    def add_points(self, points, player):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._player = player
        self._points += points
        self.set_text(f"Player {self._player}: {self._points}") #Now I can have two of the score classes and just call their player types every single time.