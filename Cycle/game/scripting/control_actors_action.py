import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)
        self._actor = 1

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        snake = cast.get_actors("cycle")
        snake[0].grow_tail(1) #This allows both snakes to keep their tails growing at all times.
        snake[1].grow_tail(1)
        

        # left
        if self._keyboard_service.is_key_down('a'):
            self._actor = 1 #This _actor var allows to see which player moved and then how to affect the cyclist in question
            self._direction = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('d'):
            self._actor = 1
            self._direction = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('w'):
            self._actor = 1
            self._direction = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('s'):
            self._actor = 1
            self._direction = Point(0, constants.CELL_SIZE)



        # left
        if self._keyboard_service.is_key_down('j'):
            self._actor = 2
            self._direction = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('l'):
            self._actor = 2
            self._direction = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('i'):
            self._actor = 2
            self._direction = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('k'):
            self._actor = 2
            self._direction = Point(0, constants.CELL_SIZE)
        

        if self._actor == 1: #This is the if statement that chooses whether red or green moves based on the input.
            snake[0].turn_head(self._direction) 
        else:
            snake[1].turn_head(self._direction)