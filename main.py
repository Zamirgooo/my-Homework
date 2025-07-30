import random

suits = [' \u2660 ', ' \u2665 ', ' \u2666', ' \u2663']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'V', 'Q', 'K', 'A']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
          '10': 10, 'V': 10, 'Q': 10, 'K': 10, 'A': 11}

def create_deck():
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def calculate_score(hand):
    score = sum(values[card[0]] for card in hand)
    aces = [card for card in hand if card[0] == 'A']
    while score > 21 and aces:
        score -= 10
        aces.pop()
    return score

def print_hand(hand, hide_first=False):
    if hide_first:
        print("Невидимая Карта, ", end='')
        print(', '.join([f'{rank}{suit}' for rank, suit in hand[1:]]))
    else:
        print(', '.join([f'{rank}{suit}' for rank, suit in hand]))

def play_blackjack():
    print("===Добро пожаловать в игру BLACKJACK===")
    deck = create_deck()

    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    print("\nВаш ход:")
    print_hand(player_hand)
    print("Счет Игрока:", calculate_score(player_hand))

    print("\nХод Диллера:")
    print_hand(dealer_hand, hide_first=True)

    while True:
        move = input("\nВы: [h] - Взять Карту, [s] - Стоп: ").lower()
        if move == 'h':
            player_hand.append(deck.pop())
            print("\nВаш Ход:")
            print_hand(player_hand)
            score = calculate_score(player_hand)
            print("Счет Игрока:", score)
            if score > 21:
                print("Перебор! Ты Пройграл(")
                return
        elif move == 's':
            break
        else:
            print("Ошибка: Введите только 'h' или же 's'")

    print("\nКарты диллера:")
    print_hand(dealer_hand)
    dealer_score = calculate_score(dealer_hand)
    while dealer_score < 17:
        dealer_hand.append(deck.pop())
        dealer_score = calculate_score(dealer_hand)

    print("\nКарты диллера::")
    print_hand(dealer_hand)
    print("Счет Диллера:", dealer_score)

    player_score = calculate_score(player_hand)

    print("\n===Результат===")
    if dealer_score > 21 or player_score > dealer_score:
        print("Вы выиграли!")
    elif player_score < dealer_score:
        print("Вы пройграли(")
    else:
        print("(Ничья)")

if __name__ == '__main__':
    while True:
        play_blackjack()
      
