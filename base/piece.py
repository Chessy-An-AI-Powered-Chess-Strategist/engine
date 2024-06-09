

class Piece:
    """
    This is the base class for all the pieces in the game.
    """
    piece_type: str
    is_white: bool
    position: tuple[int, int]
    has_moved: bool

    def get_moves(self, board, pinned) -> list[tuple[str, int]]:
        """
        Returns a list of all the possible moves for the piece.
        """
        raise NotImplementedError

    def make_move(self, move: tuple[str, int]):
        """
        Moves the piece to the given position.
        """
        raise NotImplementedError

    def undo_move(self, move: tuple[str, int]):
        """
        Undoes the move made by make_move.
        """
        raise NotImplementedError

    def is_void(self):
        """
        Returns True if the piece is a void piece, False otherwise.
        :return:
        """
        return False

    def __str__(self):
        return ("w" if self.is_white else "b") + self.piece_type



