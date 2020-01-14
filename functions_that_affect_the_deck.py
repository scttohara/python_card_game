import random


def build_deck(animals_list_of_list):
    """
    Create a list representing a deck of cards. Each
    item in the list is a dictionary representing a single card.
    """
    deck = []
    for current_row in range(len(animals_list_of_list)):
        card = {'pow_lvl': int(animals_list_of_list[current_row][0]), 'name': animals_list_of_list[current_row][1],
                'type': animals_list_of_list[current_row][2]}
        deck.append(card)

    return deck


def shuffle(deck):
    """
    Implement the Fischer-Yates Shuffle to shuffle the cards.
    https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
    """
    for i in range(len(deck) - 1, 0, -1):
        j = random.randint(0, i)
        temp = deck[j]
        deck[j] = deck[i]
        deck[i] = temp


def deal_hand(deck):
    """
    Deals two cards to each player

    @param deck: whole card deck
    @type deck: list of list
    @return: two dealt hands
    @rtype: list of dicts
    """
    player1_hand = []
    player2_hand = []
    count_of_cards_in_deck = len(deck) - 1

    for count in range(0, 4):
        random_index = random.randint(0, count_of_cards_in_deck)
        # print(random_index)
        if count == 0:
            player1_hand.append(deck[random_index])
            deck.remove(deck[random_index])
            count_of_cards_in_deck -= 1
        elif count == 2:
            player1_hand.append(deck[random_index])
            deck.remove(deck[random_index])
            count_of_cards_in_deck -= 1
        else:
            player2_hand.append(deck[random_index])
            deck.remove(deck[random_index])
            count_of_cards_in_deck -= 1

    return player1_hand, player2_hand


def trade_card_of_hand(current_player_hand, deck, player_choice):
    """
    trades the selected card for another in the deck. reduces the total deck count

    @param current_player_hand:
    @type current_player_hand: list of dicts
    @param deck: whole deck with dealt cards removed
    @type deck: list of list
    @param player_choice: players trade pick
    @type player_choice: int
    @return: none
    @rtype: none
    """
    count_of_cards_in_deck = len(deck) - 1
    random_index = random.randrange(0, count_of_cards_in_deck, 1)
    current_player_hand[player_choice - 1] = deck[random_index]
    deck.remove(deck[random_index])
