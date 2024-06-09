
from .piece import Piece


class Move:
    """
    A class to represent a move in the game.
    """

    start_position: tuple[int, int]
    end_position: tuple[int, int]
    piece: Piece
    captured_piece: Piece
    is_en_passant: bool
    is_capture: bool

    def __init__(self, piece: Piece, end_position: tuple[int, int], captured_piece: Piece = None, is_en_passant: bool = False):
        self.piece = piece
        self.start_position = piece.position
        self.end_position = end_position
        self.captured_piece = captured_piece
        self.is_en_passant = is_en_passant
        self.is_capture = captured_piece is not None