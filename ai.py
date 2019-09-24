import random
from figures import *
import sys


class Ai:

    def __init__(self, side, board):
        self.side = side
        self.board = board

    # Метод возвращает следующий ход компьютера
    def get_next_move(self):
        # Получаем список доступных ходов
        avl_moves = self.board.get_all_avl_moves(self.side)

        # Первый ход выбирается компьютером случайным образом
        moves_count = self.board.get_moves_count()
        if moves_count == 0 or moves_count == 1:
            random.seed()
            move = avl_moves[random.randint(0, len(avl_moves) - 1)]
            return move

        # Иначе нам нужно выбрать ход с максимальной оценкой
        max_rating = -sys.maxsize
        for move in avl_moves:
            self.board.apply_move(move)
            rating = self.get_rating(2, 'max', self.side, max_rating)
            self.board.cancel_move()
            if rating > max_rating:
                max_rating = rating
                move_with_max_rating = move

        # Возвращаем найденный ход
        return move_with_max_rating

    # Метод возвращает оценку хода
    # d - глубина рекурсии
    # option - что мы ищем на верхнем уровне (максимум или минимум)
    # side - сторона, для которой мы ищем максимум или минимум на верхнем уровне
    def get_rating(self, d, option, side, limit):
        if d == 0:
            return self.board.position_evaluation()

        avl_moves = self.board.get_all_avl_moves(OPPOSITE_SIDE[side])

        if option == 'max':
            min_rating = sys.maxsize
            for avl_move in avl_moves:
                self.board.apply_move(avl_move)
                rating = self.get_rating(d - 1, 'min', OPPOSITE_SIDE[side], min_rating)
                self.board.cancel_move()
                min_rating = min(min_rating, rating)
                if min_rating < limit:
                    return min_rating
            return min_rating

        if option == 'min':
            max_rating = -sys.maxsize
            for avl_move in avl_moves:
                self.board.apply_move(avl_move)
                rating = self.get_rating(d - 1, 'max', OPPOSITE_SIDE[side], max_rating)
                self.board.cancel_move()
                max_rating = max(max_rating, rating)
                if max_rating > limit:
                    return max_rating
            return max_rating
