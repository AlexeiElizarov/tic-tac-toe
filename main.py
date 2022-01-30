
def out_green(text):
    """Задает тексту зеленый цвет"""
    return "\033[32m{}\033[0m" .format(text)

def out_blue(text):
    """Задает тексту синий цвет"""
    return "\033[34m{}\033[0m" .format(text)


PLAYER = {
    'player_1': f"{out_green('X')}",
    'player_2': f"{out_blue('0')}"
}

board = {
    'line_0': [' ', 1, 2, 3],
    'line_1': [1, '-', '-', '-'],
    'line_2': [2, '-', '-', '-'],
    'line_3': [3, '-', '-', '-'],
}


def displays_game_field():
    """Выводит в консоль "Игровое поле" """
    for key in board:
        for _ in board[key]:
            print(_, end=' ')
        print()

def checks_if_the_field_is_free(vertical, horizontal):
    """Проверяет свободная ли клетка"""
    return True if board[f'line_{str(vertical)}'][horizontal] == '-' else False

def update_field(vertical, horizontal, player):
    """Сохраняет изменения на "Игровом поле" """
    if vertical == 1:
        board['line_1'][horizontal] = f"{PLAYER[player]}"
    if vertical == 2:
        board['line_2'][horizontal] = f"{PLAYER[player]}"
    if vertical == 3:
        board['line_3'][horizontal] = f"{PLAYER[player]}"
    return displays_game_field()

def new_move(player):
    while True:
        try:
            vertical, horizontal = (map(int, input(f'Введите координаты своего хода, игрок "{PLAYER[player]}" '
                                                   f'(два числа: 1,2 или 3 через пробел): ').split()))
            if checks_if_the_field_is_free(vertical, horizontal):
                update_field(vertical, horizontal, player)
                print('Принято!')
            else:
                print('Эта ячейка уже занята, выберите другую')
                new_move(player)
            print("\033[H\033[J", end="")
            break
        except:
            print('Неправильный ввод!')


def print_win(player):
    """Выводит сообщение об победе"""
    print(f"Игрок {player} выиграл!")

def checks_winning_combinations(symbol):
    """Проверяет есть ли выигрышные комбинации"""
    for i in range(1, 4):
        if board[f'line_{i}'][1] == symbol and board[f'line_{i}'][2] == symbol and board[f'line_{i}'][3] == symbol:
            return True
        if board[f'line_1'][i] == symbol and board[f'line_2'][i] == symbol and board[f'line_3'][i] == symbol:
            return True
    if board['line_1'][1] == symbol and board[f'line_2'][2] == symbol and board[f'line_3'][3] == symbol:
        return True
    if board['line_1'][3] == symbol and board[f'line_2'][2] == symbol and board[f'line_3'][1] == symbol:
        return True


def game():
    count = 0
    while True:
        new_move('player_1')
        count += 1


        if checks_winning_combinations(PLAYER['player_1']):
            print_win(PLAYER['player_1'])
            break
        if count > 8:
            print('Ничья!')
            break
        new_move('player_2')
        count += 1
        if checks_winning_combinations(PLAYER['player_2']):
            print_win(PLAYER['player_2'])
            break

if __name__ == '__main__':
    game()