from enum import Enum
from typing import List


class PieceColor(Enum):
    black = "BLACK"
    white = "WHITE"


class Board:
    def __init__(self, positions: 'Position', chess_set: 'ChessSet'):
        self._positions = positions
        self._set = chess_set


class ChessSet:
    def __init__(self, pieces: List['Piece'], board: Board):
        self._pieces = pieces
        self._board = board

    # pieces: List['Piece']
    # board: Board


def create_positions():
    h_p = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    v_p = ['8', '7', '6', '5', '4', '3', '2', '1']
    row = []
    rows = []
    for i in v_p:
        for j in h_p:
            row.append(i + j)
        rows.append(row)
        row = []

    return rows


class Position:
    """Square of the board"""
    def __init__(self, chess_board, x, y):
        self._x = x
        self._y = y
        self._board = chess_board


class Player:
    """Player of the game"""
    pass


#     should initialize with chess set
#     can move piece when its turn


class Piece:
    color: PieceColor
    chess_set: ChessSet



