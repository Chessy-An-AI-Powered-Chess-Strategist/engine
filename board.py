from base import Piece, Move
from pieces import Void, Pawn


class Board:

    _board: list[list[Piece]]

    def __init__(self):
        self._board = []

        self._board.append([Void() for _ in range(8)]) # Add the top row of void pieces.
        self._board.append([Pawn(True, (i, 1)) for i in range(8)])
        self._board.append([Void() for _ in range(8)])
        self._board.append([Void() for _ in range(8)])
        self._board.append([Void() for _ in range(8)])
        self._board.append([Void() for _ in range(8)])
        self._board.append([Pawn(False, (i, 6)) for i in range(8)])
        self._board.append([Void() for _ in range(8)])


    def __str__(self):
        return "\n".join([" ".join([str(piece) for piece in row]) for row in self._board])

