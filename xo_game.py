def show_chess(field):
    # демонстрация поля вместе с осями координат
    print("  0  1  2")
    for i in range(3):
        print(f"{i} {'  '.join(field[i])}")

def finish_game(row, col, player):
    #проверяем условия окончания игры
    a = set(xo_field[row])
    b = set([xo_field[i][col] for i in range(3)])
    c = set([xo_field[i][j] for i, j in zip(range(3), range(3))])
    d = set([xo_field[i][j] for i, j in zip(range(2, -1, -1), range(3))])
    win_check = [a, b, c, d]
    if {player} in win_check:
        show_chess(xo_field)
        print(f'Игра завершена - победу одержал {player}')
        return True
    else: #если никто еще не выиграл, проверить вариант ничьи по наличию незаполненных значений
        count = 0
        for i in xo_field:
            for j in i:
                if j == "-":
                    count += 1
        if count == 0:
            show_chess(xo_field)
            print('Игра завершена ничьей...')
            return True
    return False


while True:
    xo_field = [["-" for j in range(3)] for i in range(3)]
    xo_steps = [str(x) + str(y) for x in range(3) for y in range(3)]
    xo_player = 'X' #первый ход будет у игрока Х

    while True:
        show_chess(xo_field)
        step = input(f'Введите координату для {xo_player}:\n')
        #Проверка на корректность координат, запись и проверка на выграш хода
        if step in xo_steps:
            col, row = int(step[0]), int(step[1])
            if xo_field[row][col] == '-':
                xo_field[row][col] = xo_player
                if finish_game(row, col, xo_player):
                    q = input('Show must go on или для выхода введите +\n')
                    if q=="+":
                        exit(0)
                    break
            else:
                print(f'Уже заполненное поле значением {xo_field[row][col]}, повторите ввод для {xo_player}')
                continue
        else:
            print(f'Некорректное значение координат, повторите ввод для {xo_player}')
            continue
        #следующий ход будет выполняться другим игроком
        if xo_player == 'X':
            xo_player = 'O'
        else:
            xo_player = 'X'