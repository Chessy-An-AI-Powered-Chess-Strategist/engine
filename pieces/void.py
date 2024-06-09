from base import Piece, Move


class Void(Piece):
    """
    This class represents a void piece in the game.
    """
    def __init__(self):
        self.piece_type = "void"
        self.is_white = None
        self.position = None
        self.has_moved = None

    def get_moves(self, board, pinned) -> list[Move]:
        return []

    def make_move(self, move: Move):
        pass

    def undo_move(self, move: Move):
        pass

    def is_void(self):
        return True

    def __str__(self):
        return "Vo"