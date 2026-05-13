import random

def get_choice_name(choice):
    names = {1: "камень", 2: "ножницы", 3: "бумага"}
    return names[choice]


def get_round_winner(player, computer):
    if player == computer:
        return "draw"
    if (player == 1 and computer == 2) or \
            (player == 2 and computer == 3) or \
            (player == 3 and computer == 1):
        return "player"
    else:
        return "computer"

def play_game():
    player_wins = 0
    computer_wins = 0
    draws = 0

    print("=" * 40)
    print('КАМЕНЬ, НОЖНИЦЫ, БУМАГА')
    print("=" * 40)

    while True:
        try:
            total_rounds = int(input("\nВведите количество раундов: "))
            if total_rounds > 0:
                break
            else:
                print("Ошибка: количество раундов должно быть положительным числом.")
        except ValueError:
            print("Ошибка: пожалуйста, введите целое число.")

    print(f"\nИграем до {total_rounds} раундов. Удачи!\n")

    for round_num in range(1, total_rounds + 1):
        print("-" * 30)
        print(f"Раунд {round_num} из {total_rounds}")
        print("-" * 30)

        while True:
            print("\nВаш выбор:")
            print("1 - Камень")
            print("2 - Ножницы")
            print("3 - Бумага")
            try:
                player_choice = int(input("Введите число (1-3): "))
                if player_choice in [1, 2, 3]:
                    break
                else:
                    print("Ошибка: введите 1, 2 или 3.")
            except ValueError:
                print("Ошибка: пожалуйста, введите целое число.")

        computer_choice = random.randint(1, 3)

        print(f"\nВы выбрали: {get_choice_name(player_choice)}")
        print(f"Компьютер выбрал: {get_choice_name(computer_choice)}")

        winner = get_round_winner(player_choice, computer_choice)

        if winner == "player":
            print(">>> Вы выиграли этот раунд! <<<")
            player_wins += 1
        elif winner == "computer":
            print(">>> Компьютер выиграл этот раунд! <<<")
            computer_wins += 1
        else:
            print(">>> Ничья! <<<")
            draws += 1

        print(f"\nТекущий счет: Вы — {player_wins} | Компьютер — {computer_wins} | Ничьи — {draws}")

    print("\n" + "=" * 40)
    print("ИГРА ОКОНЧЕНА! ИТОГОВЫЙ СЧЕТ:")
    print("=" * 40)
    print(f"Ваши победы:     {player_wins}")
    print(f"Победы компьютера: {computer_wins}")
    print(f"Ничьи:           {draws}")
    print("-" * 40)

    if player_wins > computer_wins:
        print("ПОЗДРАВЛЯЕМ! ВЫ ПОБЕДИЛИ В ИГРЕ!")
    elif computer_wins > player_wins:
        print("КОМПЬЮТЕР ПОБЕДИЛ В ИГРЕ. ПОВЕЗЕТ В СЛЕДУЮЩИЙ РАЗ!")
    else:
        print("ОБЩИЙ РЕЗУЛЬТАТ — НИЧЬЯ!")

    print("=" * 40)
    print("\nСпасибо за игру!")


# Запуск игры
if __name__ == "__main__":
    play_game()