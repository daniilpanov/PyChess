# Константы сторон
WHITE = True
BLACK = False

# Имена действий, доступных для пешки
PAWN_MOVES = 'pm'
PAWN_TAKES = 'pt'

# Типы ходов
NORMAL_MOVE = 'm'  # Обычный ход
TAKE_MOVE = 't'      # Ход-взятие
CASTLING = 'o'        # Рокировка
CONVERSION = 'c'    # Превращение пешки в другую фигуру
PASSED_TAKE = 'p'  # Взятие на проходе

# Приоритеты ходов
priority_list = [TAKE_MOVE, CONVERSION, PASSED_TAKE, CASTLING, NORMAL_MOVE]


# Функция-ключ для сортировки ходов
def key_func_for_moves(move):
    return priority_list.index(move.m_type, 0, 5)

