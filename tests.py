import unittest
import animals_list
import functions_that_affect_the_deck
import score_and_round_results_handling


class CardGameTestCases(unittest.TestCase):

    # Test for deal_hand below
    # 1/5 individual functions tested
    def test_deal_hand_function(self):
        deck = functions_that_affect_the_deck.build_deck(animals_list.animals_list_function())
        functions_that_affect_the_deck.shuffle(deck)
        player1_hand, player2_hand = functions_that_affect_the_deck.deal_hand(deck)

        self.assertEqual(len(player1_hand), len(player2_hand))

    # test_get_players_att_and_def_scores_and_type_count_function
    # 2/5 individual functions tested
    def test_get_players_att_and_def_scores_and_type_count_function(self):
        player1_hand = [{'pow_lvl': '1', 'name': 'Cat', 'type': 'attacking'},
                        {'pow_lvl': '2', 'name': 'Eagle', 'type': 'attacking'}]

        player2_hand = [{'pow_lvl': '10', 'name': 'Dragon', 'type': 'attacking'},
                        {'pow_lvl': '6', 'name': 'Centaur', 'type': 'defending'}]

        self.assertEqual((3, 0, 10, 6, 2, 1),
                         score_and_round_results_handling.get_players_att_and_def_scores_and_type_count(
                             player1_hand, player2_hand))

    def test_get_players_att_and_def_scores_and_type_count_function_both_players_mixed_types(self):
        player1_hand = [{'pow_lvl': '8', 'name': 'Giant', 'type': 'attacking'},
                        {'pow_lvl': '10', 'name': 'Unicorn', 'type': 'defending'}]

        player2_hand = [{'pow_lvl': '9', 'name': 'Gryphon', 'type': 'defending'},
                        {'pow_lvl': '7', 'name': 'Vampire', 'type': 'attacking'}]

        self.assertEqual((8, 10, 7, 9, 1, 1),
                         (score_and_round_results_handling.get_players_att_and_def_scores_and_type_count(
                             player1_hand, player2_hand)))

    def test_get_players_att_and_def_scores_and_type_count_function_with_numbers_switched(self):
        player1_hand = [{'pow_lvl': '10', 'name': 'Dragon', 'type': 'attacking'},
                        {'pow_lvl': '8', 'name': 'Unicorn', 'type': 'defending'}]

        player2_hand = [{'pow_lvl': '9', 'name': 'Werewolf', 'type': 'attacking'},
                        {'pow_lvl': '7', 'name': 'Hippogriff', 'type': 'defending'}]

        self.assertEqual((10, 8, 9, 7, 1, 1),
                         (score_and_round_results_handling.get_players_att_and_def_scores_and_type_count(
                             player1_hand, player2_hand)))

    # test_coordinate_score_calc_and_get_round_result
    # 3/5 individual functions tested
    def test_coordinate_score_calc_and_get_round_result_player2_winner(self):
        player1_hand = [{'pow_lvl': '4', 'name': 'Sea Serpent', 'type': 'attacking'},
                        {'pow_lvl': '5', 'name': 'Gargoyle', 'type': 'attacking'}]

        player2_hand = [{'pow_lvl': '7', 'name': 'Vampire', 'type': 'attacking'},
                        {'pow_lvl': '3', 'name': 'Gnome', 'type': 'defending'}]

        # 1 means player 2 is winner
        self.assertEqual((1, 6, 7), score_and_round_results_handling.coordinate_score_calc_and_get_round_result(
            player1_hand, player2_hand))

    def test_coordinate_score_calc_and_get_round_result_draw_two_att_other_player_has_mixed_types(self):
        player1_hand = [{'pow_lvl': '2', 'name': 'Eagle', 'type': 'attacking'},
                        {'pow_lvl': '6', 'name': 'Hydra', 'type': 'attacking'}]

        player2_hand = [{'pow_lvl': '7', 'name': 'Vampire', 'type': 'attacking'},
                        {'pow_lvl': '1', 'name': 'Dog', 'type': 'defending'}]

        # 2 equals draw
        self.assertEqual((2, 7, 7), score_and_round_results_handling.coordinate_score_calc_and_get_round_result(
            player1_hand, player2_hand))

    def test_coordinate_score_calc_and_get_round_result_player1_winner_all_attacking(self):
        player1_hand = [{'pow_lvl': '2', 'name': 'Eagle', 'type': 'attacking'},
                        {'pow_lvl': '6', 'name': 'Hydra', 'type': 'attacking'}]

        player2_hand = [{'pow_lvl': '4', 'name': 'Sea Serpent', 'type': 'attacking'},
                        {'pow_lvl': '3', 'name': 'Liger', 'type': 'attacking'}]

        # 0 means player 1 won
        self.assertEqual((0, 8, 7), score_and_round_results_handling.coordinate_score_calc_and_get_round_result(
            player1_hand, player2_hand))

    def test_coordinate_score_calc_and_get_round_result_two_attack_vs_two_defending(self):
        player1_hand = [{'pow_lvl': '3', 'name': 'Liger', 'type': 'attacking'},
                        {'pow_lvl': '10', 'name': 'Dragon', 'type': 'attacking'}]

        player2_hand = [{'pow_lvl': '9', 'name': 'Gryphon', 'type': 'defending'},
                        {'pow_lvl': '10', 'name': 'Unicorn', 'type': 'defending'}]

        # 1 equals player 2 winner
        self.assertEqual((1, 13, 19), score_and_round_results_handling.coordinate_score_calc_and_get_round_result(
            player1_hand, player2_hand))

    def test_coordinate_score_calc_and_get_round_result_player2_winner_bigger_numbers(self):
        player1_hand = [{'pow_lvl': '8', 'name': 'Giant', 'type': 'attacking'},
                        {'pow_lvl': '1', 'name': 'Dog', 'type': 'defending'}]

        player2_hand = [{'pow_lvl': '7', 'name': 'Vampire', 'type': 'attacking'},
                        {'pow_lvl': '3', 'name': 'Gnome', 'type': 'defending'}]
        # 1 equals player 2 winner
        self.assertEqual((1, 5, 6), score_and_round_results_handling.coordinate_score_calc_and_get_round_result(
            player1_hand, player2_hand))

    def test_coordinate_score_calc_and_get_round_result_will_be_draw_players_att_and_def_cards(self):
        player1_hand = [{'pow_lvl': '8', 'name': 'Giant', 'type': 'attacking'},
                        {'pow_lvl': '3', 'name': 'Gnome', 'type': 'defending'}]

        player2_hand = [{'pow_lvl': '7', 'name': 'Vampire', 'type': 'attacking'},
                        {'pow_lvl': '4', 'name': 'Mermaid', 'type': 'defending'}]

        # 2 equals draw
        self.assertEqual((2, 4, 4), score_and_round_results_handling.coordinate_score_calc_and_get_round_result(
            player1_hand, player2_hand))

    def test_coordinate_score_calc_and_get_round_result(self):
        player1_hand = [{'pow_lvl': '8', 'name': 'Giant', 'type': 'attacking'},
                        {'pow_lvl': '10', 'name': 'Unicorn', 'type': 'defending'}]

        player2_hand = [{'pow_lvl': '9', 'name': 'Giant', 'type': 'attacking'},
                        {'pow_lvl': '7', 'name': 'Hippogriff', 'type': 'defending'}]

        # 0 equals player 1 winner
        self.assertEqual((0, 1, -1), score_and_round_results_handling.coordinate_score_calc_and_get_round_result(
            player1_hand, player2_hand))

    # Test different situations with 11 as the value for both or one player
    def test_coordinate_score_calc_and_get_round_result_with_both_players_having_11_all_attacking(self):
        player1_hand = [{'pow_lvl': '1', 'name': 'Cat', 'type': 'attacking'},
                        {'pow_lvl': '10', 'name': 'Dragon', 'type': 'attacking'}]

        player2_hand = [{'pow_lvl': '8', 'name': 'Giant', 'type': 'attacking'},
                        {'pow_lvl': '3', 'name': 'Liger', 'type': 'attacking'}]

        # 0 equals player 1 winner
        self.assertEqual((0, 11, 11), score_and_round_results_handling.coordinate_score_calc_and_get_round_result(
            player1_hand, player2_hand))

    def test_coordinate_score_calc_and_get_round_result_with_both_players_having_11_all_defending(self):
        player1_hand = [{'pow_lvl': 2, 'name': 'Owl', 'type': 'defending'},
                        {'pow_lvl': 9, 'name': 'Gryphon', 'type': 'defending'}]

        player2_hand = [{'pow_lvl': 10, 'name': 'Unicorn', 'type': 'defending'},
                        {'pow_lvl': 1, 'name': 'Dog', 'type': 'defending'}]

        # 1 equals player 2 winner
        self.assertEqual((1, 11, 11), score_and_round_results_handling.coordinate_score_calc_and_get_round_result(
            player1_hand, player2_hand))

    def test_coordinate_score_calc_and_get_round_result_with_one_player1_having_11_all_defending(self):
        player1_hand = [{'pow_lvl': 2, 'name': 'Owl', 'type': 'defending'},
                        {'pow_lvl': 9, 'name': 'Gryphon', 'type': 'defending'}]

        player2_hand = [{'pow_lvl': 3, 'name': 'Gnome', 'type': 'defending'},
                        {'pow_lvl': 1, 'name': 'Dog', 'type': 'defending'}]

        # 0 equals player 1 winner
        self.assertEqual((0, 11, 4), score_and_round_results_handling.coordinate_score_calc_and_get_round_result(
            player1_hand, player2_hand))

    def test_coordinate_score_calc_and_get_round_result_all_defending_type(self):
        player1_hand = [{'pow_lvl': '9', 'name': 'Gryphon', 'type': 'defending'},
                        {'pow_lvl': '1', 'name': 'Dog', 'type': 'defending'}]

        player2_hand = [{'pow_lvl': '6', 'name': 'Centaur', 'type': 'defending'},
                        {'pow_lvl': '3', 'name': 'Gnome', 'type': 'defending'}]

        # 2 equals draw
        self.assertEqual((2, 10, 9), score_and_round_results_handling.coordinate_score_calc_and_get_round_result(
            player1_hand, player2_hand))

    # Test both_players_have_only_defending function
    # 4/5 individual functions tested
    def test_both_players_have_only_defending(self):
        player1_hand = [{'pow_lvl': '9', 'name': 'Gryphon', 'type': 'defending'},
                        {'pow_lvl': '1', 'name': 'Dog', 'type': 'defending'}]

        player2_hand = [{'pow_lvl': '6', 'name': 'Centaur', 'type': 'defending'},
                        {'pow_lvl': '3', 'name': 'Gnome', 'type': 'defending'}]
        player1_defense_score = 10
        player2_defense_score = 9

        # 2 equals draw
        self.assertEqual(2,
                         score_and_round_results_handling.both_players_have_only_defending(player1_defense_score,
                                                                                           player2_defense_score,
                                                                                           player1_hand,
                                                                                           player2_hand))

    def test_both_players_have_only_defending_bigger_numbers(self):
        player1_hand = [{'pow_lvl': '9', 'name': 'Gryphon', 'type': 'defending'},
                        {'pow_lvl': '6', 'name': 'Centaur', 'type': 'defending'}]

        player2_hand = [{'pow_lvl': '10', 'name': 'Unicorn', 'type': 'defending'},
                        {'pow_lvl': '3', 'name': 'Gnome', 'type': 'defending'}]
        player1_defense_score = 15
        player2_defense_score = 13

        # 2 equals draw
        self.assertEqual(2,
                         score_and_round_results_handling.both_players_have_only_defending(player1_defense_score,
                                                                                           player2_defense_score,
                                                                                           player1_hand,
                                                                                           player2_hand))

    def test_both_players_have_only_defending_player_one_has_11_and_higher_def_total(self):
        player1_hand = [{'pow_lvl': '9', 'name': 'Gryphon', 'type': 'defending'},
                        {'pow_lvl': '2', 'name': 'Owl', 'type': 'defending'}]

        player2_hand = [{'pow_lvl': '6', 'name': 'Centaur', 'type': 'defending'},
                        {'pow_lvl': '3', 'name': 'Gnome', 'type': 'defending'}]
        player1_defense_score = 11
        player2_defense_score = 9

        # 0 means player 1 wins
        self.assertEqual(0,
                         score_and_round_results_handling.both_players_have_only_defending(player1_defense_score,
                                                                                           player2_defense_score,
                                                                                           player1_hand,
                                                                                           player2_hand))

    def test_both_players_have_only_defending_player_one_has_11_but_has_lower_def_total(self):
        player1_hand = [{'pow_lvl': '9', 'name': 'Gryphon', 'type': 'defending'},
                        {'pow_lvl': '2', 'name': 'Owl', 'type': 'defending'}]

        player2_hand = [{'pow_lvl': '6', 'name': 'Centaur', 'type': 'defending'},
                        {'pow_lvl': '8', 'name': 'Sphinx', 'type': 'defending'}]
        player1_defense_score = 11
        player2_defense_score = 14

        # 0 means player 1 wins
        self.assertEqual(0,
                         score_and_round_results_handling.both_players_have_only_defending(player1_defense_score,
                                                                                           player2_defense_score,
                                                                                           player1_hand,
                                                                                           player2_hand))

    def test_both_players_have_only_defending_player_one_has_11_and_other_player_has_11_player1_should_win(self):
        player1_hand = [{'pow_lvl': '9', 'name': 'Gryphon', 'type': 'defending'},
                        {'pow_lvl': '2', 'name': 'Owl', 'type': 'defending'}]

        player2_hand = [{'pow_lvl': '3', 'name': 'Gnome', 'type': 'defending'},
                        {'pow_lvl': '8', 'name': 'Sphinx', 'type': 'defending'}]
        player1_defense_score = 11
        player2_defense_score = 11

        # 0 means player 1 wins
        self.assertEqual(0,
                         score_and_round_results_handling.both_players_have_only_defending(player1_defense_score,
                                                                                           player2_defense_score,
                                                                                           player1_hand,
                                                                                           player2_hand))

    def test_both_players_have_only_defending_player_one_has_11_and_other_player_has_11_player2_should_win(self):
        player1_hand = [{'pow_lvl': '3', 'name': 'Gnome', 'type': 'defending'},
                        {'pow_lvl': '8', 'name': 'Sphinx', 'type': 'defending'}]

        player2_hand = [{'pow_lvl': '9', 'name': 'Gryphon', 'type': 'defending'},
                        {'pow_lvl': '2', 'name': 'Owl', 'type': 'defending'}]
        player1_defense_score = 11
        player2_defense_score = 11

        # 1 means player 2 wins
        self.assertEqual(1,
                         score_and_round_results_handling.both_players_have_only_defending(player1_defense_score,
                                                                                           player2_defense_score,
                                                                                           player1_hand,
                                                                                           player2_hand))

    # Test both_players_have_only_attacking function
    # 5/5 individual functions tested
    def test_both_players_have_only_attacking_and_both_have_11_p1_should_win(self):
        player1_hand = [{'pow_lvl': '1', 'name': 'Cat', 'type': 'attacking'},
                        {'pow_lvl': '10', 'name': 'Dragon', 'type': 'attacking'}]

        player2_hand = [{'pow_lvl': '8', 'name': 'Giant', 'type': 'attacking'},
                        {'pow_lvl': '3', 'name': 'Ligar', 'type': 'attacking'}]
        player1_attack_score = 11
        player2_attack_score = 11

        # 0 equals player 1 winner
        self.assertEqual(0, score_and_round_results_handling.both_players_have_only_attacking(player1_attack_score,
                                                                                              player2_attack_score,
                                                                                              player1_hand,
                                                                                              player2_hand))

    def test_both_players_have_only_attacking_and_both_have_11_p2_should_win(self):
        player1_hand = [{'pow_lvl': '8', 'name': 'Giant', 'type': 'attacking'},
                        {'pow_lvl': '3', 'name': 'Ligar', 'type': 'attacking'}]

        player2_hand = [{'pow_lvl': '1', 'name': 'Cat', 'type': 'attacking'},
                        {'pow_lvl': '10', 'name': 'Dragon', 'type': 'attacking'}]
        player1_attack_score = 11
        player2_attack_score = 11

        # 1 means player 2 wins
        self.assertEqual(1, score_and_round_results_handling.both_players_have_only_attacking(player1_attack_score,
                                                                                              player2_attack_score,
                                                                                              player1_hand,
                                                                                              player2_hand))

    def test_both_players_have_only_attacking_p1_has_11(self):
        player1_hand = [{'pow_lvl': '9', 'name': 'Werewolf', 'type': 'attacking'},
                        {'pow_lvl': '2', 'name': 'Eagle', 'type': 'attacking'}]

        player2_hand = [{'pow_lvl': '1', 'name': 'Cat', 'type': 'attacking'},
                        {'pow_lvl': '8', 'name': 'Giant', 'type': 'attacking'}]
        player1_attack_score = 11
        player2_attack_score = 9

        # 0 equals player 1 winner
        self.assertEqual(0, score_and_round_results_handling.both_players_have_only_attacking(player1_attack_score,
                                                                                              player2_attack_score,
                                                                                              player1_hand,
                                                                                              player2_hand))

    def test_both_players_have_only_attacking_p2_has_11s(self):
        player1_hand = [{'pow_lvl': '1', 'name': 'Cat', 'type': 'attacking'},
                        {'pow_lvl': '8', 'name': 'Giant', 'type': 'attacking'}]

        player2_hand = [{'pow_lvl': '9', 'name': 'Werewolf', 'type': 'attacking'},
                        {'pow_lvl': '2', 'name': 'Eagle', 'type': 'attacking'}]
        player1_attack_score = 9
        player2_attack_score = 11

        # 1 means player 2 wins
        self.assertEqual(1, score_and_round_results_handling.both_players_have_only_attacking(player1_attack_score,
                                                                                              player2_attack_score,
                                                                                              player1_hand,
                                                                                              player2_hand))

    def test_both_players_have_only_attacking_no_11s_p2_wins(self):
        player1_hand = [{'pow_lvl': '1', 'name': 'Cat', 'type': 'attacking'},
                        {'pow_lvl': '7', 'name': 'Vampire', 'type': 'attacking'}]

        player2_hand = [{'pow_lvl': '9', 'name': 'Werewolf', 'type': 'attacking'},
                        {'pow_lvl': '6', 'name': 'Hydra', 'type': 'attacking'}]
        player1_attack_score = 8
        player2_attack_score = 15

        # 1 means player 2 wins
        self.assertEqual(1, score_and_round_results_handling.both_players_have_only_attacking(player1_attack_score,
                                                                                              player2_attack_score,
                                                                                              player1_hand,
                                                                                              player2_hand))

    def test_both_players_have_only_attacking_no_11s_p1_wins(self):
        player1_hand = [{'pow_lvl': '10', 'name': 'Dragon', 'type': 'attacking'},
                        {'pow_lvl': '7', 'name': 'Vampire', 'type': 'attacking'}]

        player2_hand = [{'pow_lvl': '9', 'name': 'Werewolf', 'type': 'attacking'},
                        {'pow_lvl': '6', 'name': 'Hydra', 'type': 'attacking'}]
        player1_attack_score = 17
        player2_attack_score = 15

        # 0 means player 1 wins
        self.assertEqual(0, score_and_round_results_handling.both_players_have_only_attacking(player1_attack_score,
                                                                                              player2_attack_score,
                                                                                              player1_hand,
                                                                                              player2_hand))


if __name__ == '__main__':
    unittest.main()

"""
    animals_list = [['1', 'Cat', 'attacking'], ['2', 'Eagle', 'attacking'],
                        ['3', 'Liger', 'attacking'], ['4', 'Sea Serpent', 'attacking'],
                        ['5', 'Gargoyle', 'attacking'], ['6', 'Hydra', 'attacking'],
                        ['7', 'Vampire', 'attacking'], ['8', 'Giant', 'attacking'],
                        ['9', 'Werewolf', 'attacking'], ['10', 'Dragon', 'attacking'],
                        ['1', 'Dog', 'defending'], ['2', 'Owl', 'defending'],
                        ['3', 'Gnome', 'defending'], ['4', 'Mermaid', 'defending'],
                        ['5', 'Fairy', 'defending'], ['6', 'Centaur', 'defending'],
                        ['7', 'Hippogriff', 'defending'], ['8', 'Sphinx', 'defending'],
                        ['9', 'Gryphon', 'defending'], ['10', 'Unicorn', 'defending']]
"""
