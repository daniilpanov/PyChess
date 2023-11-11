# Частота кадров
FPS = 5

# Константы сторон
WHITE = True
BLACK = False

# Цвета для белых и черных клеток
WHITE_CELL_COLOR = (230, 230, 230)
BLACK_CELL_COLOR = (150, 150, 150)

# Имена действий, доступных для пешки
PAWN_MOVES = 'pawn_moves'
PAWN_TAKES = 'pawn_takes'

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


# Варианты завершения игры
MAT = 'mat'  # Игра завершилась матом
PAT = 'pat'  # Игра завершилась патом
