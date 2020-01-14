from time import sleep
from functions_that_affect_the_deck import trade_card_of_hand
from score_and_round_results_handling import get_players_att_and_def_scores_and_type_count


def display_welcome():
    print("______________________________________________\n"
          "_________________WELCOME TO___________________\n"
          "_______________MAGICAL ANIMALS________________\n"
          "________________THE CARD GAME_________________\n"
          "______________________________________________\n")
    sleep(4)  # slows down the stuff being printed to the screen


def start_question():
    """

    @return: start_game_type: either 1 to load saved results, 2 for new game, 0 to quit
    @rtype: int
    """
    start_game_type = 0
    keep_asking = 1
    while keep_asking == 1:
        try:
            path_choice = int(input("Would you like to:\n0. quit\n"
                                    "1. load last saved game results\n2. Reset past game results "
                                    "(Appends to 'results_record.txt', will not overwrite past results)"
                                    "\n\nEnter 0 to quit, 1 to load, 2 for new:\n"))
            if path_choice == 0:
                start_game_type = 0
                keep_asking = 0
            elif path_choice == 1:
                start_game_type = 1
                keep_asking = 0
            elif path_choice == 2:
                start_game_type = 2
                keep_asking = 0
            else:
                raise ValueError
        except ValueError:
            print("That isn't a 0, 1, or 2\nPlease try again")
            continue

    return start_game_type


def print_past_results(records_list_of_lists):
    """
    prints past results. sleep(2) after to slow down how fast things print to screen.

    @param records_list_of_lists: records list
    @type records_list_of_lists: list of lists
    @return: none.
    @rtype: none.
    """
    print('\nThe past game results are:\nPlayer 1 has {} wins\nPlayer 2 has {} wins\n'
          'There are {} draws'.format(records_list_of_lists[-3][1], records_list_of_lists[-2][1],
                                      records_list_of_lists[-1][1]))
    sleep(2)  # slows down the stuff being printed to the screen


def print_deck_being_shuffled():
    """
    prints that the deck is being shuffled and them some dots again just to slow the game down a little bit
    Made it feel more real.
    @return: none
    @rtype: none
    """
    print("\nThe deck is being shuffled, hands will be dealt shortly")
    sleep(3)  # slows down the stuff being printed to the screen
    print(".")
    sleep(1)
    print(".")
    sleep(1)
    print(".")
    sleep(1)


def print_players_scores(player1_hand, player2_hand):
    """

    @param player1_hand: player 1's current cards
    @type player1_hand: list of lists
    @param player2_hand: player 2's current cards
    @type player2_hand: list of lists
    @return: none
    @rtype: none
    """
    # get player current scores function
    get_players_scores_list = get_players_att_and_def_scores_and_type_count(player1_hand, player2_hand)

    # below unpacks the results from the function above. results put in list to shorten the length of the two lines of code
    p1_attack_score, p1_def_score, p2_attack_score, p2_def_score, p1_attacking_card_count, p2_attacking_card_count = get_players_scores_list

    print('\nPlayer 1 has been dealt:\nCard 1: {}, power lvl: {} ({})\nCard 2: {}, power lvl: {} ({})'.format(
        player1_hand[0]['name'], player1_hand[0]['pow_lvl'], player1_hand[0]['type'], player1_hand[1]['name'],
        player1_hand[1]['pow_lvl'], player1_hand[1]['type']))

    print('Attacking score {}\nDefending score {}'.format(p1_attack_score, p1_def_score))

    print('\nPlayer 2 has been dealt:\nCard 1: {}, power lvl: {} ({})\nCard 2: {}, power lvl: {} ({})'.format(
        player2_hand[0]['name'], player2_hand[0]['pow_lvl'], player2_hand[0]['type'], player2_hand[1]['name'],
        player2_hand[1]['pow_lvl'], player2_hand[1]['type']))

    print('Attacking score {}\nDefending score {}'.format(p2_attack_score, p2_def_score))
    sleep(1)  # slows down the stuff being printed to the screen


def player_pick(player_number, deck, current_player_hand):
    """
    prompts players to pick trade or stick and handles exceptions.
    returns a boolean represented if the player decided to trade or not

    @param player_number: current player, either 1 or 2
    @type player_number: int
    @param deck: the deck with the cards already dealt removed
    @type deck: list of list
    @param current_player_hand:
    @type current_player_hand: list of dicts
    @return: decided_to_trade:
    @rtype: boolean
    """
    pick_is_valid = False
    number_is_valid = False
    decided_to_trade = False

    while not pick_is_valid:
        try:
            player_trade_or_stick = (input("\nPlayer {}, trade or stick? (enter 'trade' or 't' for trade,"
                                           " 'stick' or 's' for stick)\n".format(player_number))).lower()
            if player_trade_or_stick == 'trade' or player_trade_or_stick == 't':
                pick_is_valid = True
                while not number_is_valid:
                    try:
                        player_choice = int(input("Card to trade? (enter card number. i.e. '1' or '2')\n"))
                        if player_choice == 1:
                            # trade card 1 logic
                            # below function is from functions_that_affect_the_deck import above
                            trade_card_of_hand(current_player_hand, deck, player_choice)
                            number_is_valid = True
                            decided_to_trade = True
                        elif player_choice == 2:
                            # trade card 2 logic here
                            # below function is from functions_that_affect_the_deck import above
                            trade_card_of_hand(current_player_hand, deck, player_choice)
                            number_is_valid = True
                            decided_to_trade = True
                        else:
                            raise ValueError
                    except ValueError:
                        print("That is not a 1 or a 2, please try again")
                        continue
            elif player_trade_or_stick == 'stick' or player_trade_or_stick == 's':
                pick_is_valid = True
            else:
                raise ValueError
        except ValueError:
            print("The options are 'trade' and 'stick' (enter 'trade' or 't' for trade,"
                  " 'stick' or 's' for stick), please try again")
            continue

        return decided_to_trade


def print_winner(winner, player1_final_score, player2_final_score):
    """

    @param winner: indicates winner
    @type winner: int
    @param player1_final_score:
    @type player1_final_score: int
    @param player2_final_score:
    @type player2_final_score: int
    @return: none.
    @rtype: none.
    """
    # update scores below is done
    if winner == 2:  # draw
        print("\nPlayer 1's final score is {} and Player 2's final score is {}. "
              "The result is a draw!!".format(player1_final_score, player2_final_score))
    elif winner == 1:  # player 2 wins
        print("\nPlayer 1's final score is {} and Player 2's final score is {}. "
              "Player 2 wins!!".format(player1_final_score, player2_final_score))
    else:  # player 1 wins
        print("\nPlayer 1's final score is {} and Player 2's final score is {}. "
              "Player 1 wins!!".format(player1_final_score, player2_final_score))
        sleep(1)  # slows down the stuff being printed to the screen


def ask_user_if_they_want_to_continue():
    """
    check if user wants to quit below

    @return: keep_playing: users choice whether to keep playing or quit.
    @rtype: int
    """

    keep_asking = True
    while keep_asking:
        try:
            keep_playing = int(input("\nWould you like to quit or play again? (Enter 0 to quit, 1 to play again)\n"))
            if keep_playing == 1:
                keep_asking = False
            elif keep_playing == 0:
                keep_asking = False
            else:
                raise ValueError
        except ValueError:
            print("\nThis is not a '0' or '1', please try again\n")
            continue

    return keep_playing
