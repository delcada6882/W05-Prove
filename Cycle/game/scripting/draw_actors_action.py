import constants
from game.shared.point import Point
from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        score = cast.get_actors("scores")
        snake = cast.get_actors("cycle")
        
        segments = snake[0].get_segments()
        segments2 = snake[1].get_segments()
        messages = cast.get_actors("messages")


        x = int(constants.MAX_X - constants.CELL_SIZE * 8) #This right here moves the "Player Two" to the right of the screen.
        y = int(constants.MAX_Y - constants.CELL_SIZE * 40) 
        score[1].set_position(Point(x, y))

        self._video_service.clear_buffer()
        self._video_service.draw_actors(segments)
        self._video_service.draw_actors(segments2) #had to add another snake drawer
        self._video_service.draw_actor(score[0])
        self._video_service.draw_actor(score[1]) #had to add another score drawer
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()