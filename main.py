"""
Entry point for card game

"""
import read_and_write_to_file_functions
import functions_that_affect_the_deck
from time import time
import functions_that_print_to_the_screen
import score_and_round_results_handling


def main():
    """
    entry point of program. Just calls functions no real logic handled here

    @return: none
    @rtype: none
    """
    functions_that_print_to_the_screen.display_welcome()
    animals_list_of_lists = read_and_write_to_file_functions.get_animal_names()
    path_choice = functions_that_print_to_the_screen.start_question()

    if path_choice == 1 or path_choice == 2:
        keep_playing = 1
        while keep_playing == 1:
            # Create deck
            deck = functions_that_affect_the_deck.build_deck(animals_list_of_lists)

            # shuffle deck
            functions_that_affect_the_deck.shuffle(deck)

            # Get past game results
            results_record, player1_win_count, player2_win_count, draws = read_and_write_to_file_functions.get_game_results_record(path_choice)

            # one round play logic below
            # print past results
            functions_that_print_to_the_screen.print_past_results(results_record[-3:])

            # tell user deck is being shuffled
            functions_that_print_to_the_screen.print_deck_being_shuffled()

            # deal hands to the two players
            player1_hand, player2_hand = functions_that_affect_the_deck.deal_hand(deck)

            # print player scores functions
            functions_that_print_to_the_screen.print_players_scores(player1_hand, player2_hand)

            # does player 1 want to trade or stick? does player 2 want to trade or stick? should go under this (here)
            # Trade or stick function below
            check_decided_to_trade_player1 = functions_that_print_to_the_screen.player_pick(1, deck, player1_hand)
            check_decided_to_trade_player2 = functions_that_print_to_the_screen.player_pick(2, deck, player2_hand)

            # if one picks trade then need to re-print cards and re-calculate scores
            if check_decided_to_trade_player1 or check_decided_to_trade_player2:

                functions_that_print_to_the_screen.print_players_scores(player1_hand, player2_hand)

            # calculate scores and winner function here
            return_list_coordinate = score_and_round_results_handling.coordinate_score_calc_and_get_round_result(player1_hand, player2_hand)

            winner, player1_final_score, player2_final_score = return_list_coordinate

            # Prints winner to screen...also adds to the winners record for saving to the external file
            functions_that_print_to_the_screen.print_winner(winner, player1_final_score, player2_final_score)

            # increase win count or draw count depending results
            player1_win_count, player2_win_count, draws = score_and_round_results_handling.increase_wins_or_draw_count(
                winner, player1_win_count, player2_win_count, draws)

            # writes score to file logic below
            read_and_write_to_file_functions.write_game_results_record_to_file(results_record, player1_win_count, player2_win_count, draws)

            # loads game results from text file
            results_record, player1_win_count, player2_win_count, draws = read_and_write_to_file_functions.get_game_results_record()

            # print past results
            functions_that_print_to_the_screen.print_past_results(results_record[-3:])

            # check if user wants to quit below
            keep_playing = functions_that_print_to_the_screen.ask_user_if_they_want_to_continue()
            path_choice = 1

    elif path_choice == 0:
        print("Shutting down")


if __name__ == '__main__':
    start_time = time()
    main()
    end_time = time() - start_time
    # print('\n\n--- {} seconds ---'.format(end_time))
