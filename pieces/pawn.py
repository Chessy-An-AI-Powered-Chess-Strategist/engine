from base import Piece, Move


class Pawn(Piece):
    """
    This class represents a pawn in the game.
    """
    en_passant: bool

    def __init__(self, is_white: bool, position: tuple[int, int]):
        self.piece_type = "P"
        self.is_white = is_white
        self.position = position
        self.has_moved = False
        self.en_passant = False

    def get_moves(self, board, pinned) -> list[Move]:
        moves = []
        x, y = self.position

        direction_modifier = 1 if self.is_white else -1 # The direction the pawn moves in.

        # Check if the pawn is in pinned pieces
        if self.position in pinned:
            return moves

        # Check if the pawn can move forward by one.
        if board[x][y + direction_modifier] is None: # ToDo: Replace with the void piece.
            moves.append((x, y + direction_modifier))

            # Check if the pawn can move forward by two.
            if not self.has_moved and board[x][y + 2 * direction_modifier] is None:
                moves.append((x, y + 2 * direction_modifier))

        return moves



