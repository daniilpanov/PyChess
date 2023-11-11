import os

from free_chess_lib.boards import Board
from free_chess_lib.params import *


class Figure:
    type: str
    col: int
    row: int
    side: bool
    board: Board
    is_drop: bool

    def __init__(self, _type, r: int, c: int, side, board):
        self.type = _type
        self.row = r
        self.col = c
        self.side = side
        self.board = board
        self.is_drop = False

    def set_pos(self, r, c):
        self.row = r
        self.col = c

    @staticmethod
    def is_valid_pos(r, c):
        if 0 <= r <= 7 and 0 <= c <= 7:
            return True
        else:
            return False


class King(Figure):

    def __init__(self, r, c, side, board):
        Figure.__init__(self, 'k', r, c, side, board)

    def get_actions(self):
        result = []
        offsets = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]

        for delta_row, delta_col in offsets:
            r1 = self.row + delta_row
            c1 = self.col + delta_col
            if not self.is_valid_pos(r1, c1):
                continue
            result.append((r1, c1))

        # Возвращаем результат
        return result


class Queen(Figure):

    def __init__(self, r, c, side, board):
        Figure.__init__(self, 'q', r, c, side, board)

    def get_actions(self):
        result = []
        offsets = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]

        for delta_row, delta_col in offsets:
            mul = 0
            while True:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break

        # Возвращаем результат
        return result


class Rook(Figure):

    def __init__(self, r, c, side, board):
        Figure.__init__(self, 'r', r, c, side, board)

    def get_actions(self):
        result = []
        offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for delta_row, delta_col in offsets:
            mul = 0
            while True:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break

        # Возвращаем результат
        return result


class Bishop(Figure):

    def __init__(self, r, c, side, board):
        Figure.__init__(self, 'b', r, c, side, board)

    def get_actions(self):
        result = []
        offsets = [(-1, 1), (1, 1), (1, -1), (-1, -1)]

        for delta_row, delta_col in offsets:
            mul = 0
            while True:
                mul += 1
                r1 = self.row + mul * delta_row
                c1 = self.col + mul * delta_col
                if not self.is_valid_pos(r1, c1):
                    break
                result.append((r1, c1))
                figure = self.board.get_figure(r1, c1)
                if figure is not None:
                    break

        # Возвращаем результат
        return result


class Knight(Figure):

    def __init__(self, r, c, side, board):
        Figure.__init__(self, 'k', r, c, side, board)

    def get_actions(self):
        result = []

        offsets = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
        for delta_row, delta_col in offsets:
            r1 = self.row + delta_row
            c1 = self.col + delta_col
            if not self.is_valid_pos(r1, c1):
                continue
            result.append((r1, c1))

        # Возвращаем результат
        return result


class Pawn(Figure):

    def __init__(self, r, c, side, board):
        Figure.__init__(self, 'p', r, c, side, board)

        # Выбираем направление движения пешки в зависимости от того, где находится её стартовая позиция
        if self.row == 1:
            self.direction = 1
        if self.row == 6:
            self.direction = -1

    def get_actions(self, *args):
        result = []

        if PAWN_MOVES in args or not args:
            # Проверяем возможность хода на одну клетку вперед
            r1 = self.row + self.direction
            c = self.col
            if self.is_valid_pos(r1, c):
                if self.board.get_figure(r1, c) is None:
                    result.append((r1, c))

            # Проверяем возможность хода на две клетки вперед
            if self.row == 1 or self.row == 6:
                r2 = self.row + 2 * self.direction
                if self.is_valid_pos(r2, c):
                    if self.board.get_figure(r1, c) is None and self.board.get_figure(r2, c) is None:
                        result.append((r2, c))

        if PAWN_TAKES in args or not args:
            # Ищем взятия (за исключением взятия на проходе, которое требует информации о предыдущем ходе) и защиты
            offsets = (-1, 1)
            r1 = self.row + self.direction
            for offset in offsets:
                c1 = self.col + offset
                if not self.is_valid_pos(r1, c1):
                    continue
                result.append((r1, c1))

        # Возвращаем результат
        return result
