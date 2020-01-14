def increase_wins_or_draw_count(winner, player1, player2, draws):
    """
    updates win scores
    @return: player1 win count, player2 win count, draw count
    @rtype: tuple
    """
    if winner == 2:  # draw
        draws += 1
    elif winner == 1:  # player 2 wins
        player2 += 1
    else:  # player 1 wins
        player1 += 1

    return player1, player2, draws


def get_players_att_and_def_scores_and_type_count(player1_hand, player2_hand):
    """
    get the current attack and defense scores for each player and the count of the type of cards they both have

    @param player1_hand: player 1's hand
    @type player1_hand: list of dict
    @param player2_hand: player 2's hand
    @type player2_hand: list of dict
    @return: player 1 and 2's current attack and def scores and the count of the type of cards they have
    @rtype: tuple
    """
    p1_attack_score = p1_def_score = p2_attack_score = 0
    p2_def_score = p1_attacking_card_count = p2_attacking_card_count = 0

    # Player 1
    if player1_hand[0]['type'] == player1_hand[1]['type'] and player1_hand[0]['type'] == 'attacking':  # two att p1
        p1_attack_score = int(player1_hand[0]['pow_lvl']) + int(player1_hand[1]['pow_lvl'])
        p1_attacking_card_count = 2

    elif player1_hand[0]['type'] == player1_hand[1]['type'] and player1_hand[0]['type'] == 'defending':  # two def p1
        p1_def_score = int(player1_hand[0]['pow_lvl']) + int(player1_hand[1]['pow_lvl'])
        p1_attacking_card_count = 0
    elif player1_hand[0]['type'] != player1_hand[1]['type']:  # one attack/one defend for p1
        p1_attacking_card_count = 1
        if player1_hand[0]['type'] == 'attacking':
            p1_attack_score = int(player1_hand[0]['pow_lvl'])  # sets attacking animal score
            p1_def_score = int(player1_hand[1]['pow_lvl'])  # sets defending animal score
        else:
            p1_def_score = int(player1_hand[0]['pow_lvl'])  # sets defending animal score
            p1_attack_score = int(player1_hand[1]['pow_lvl'])  # sets attacking animal score

    # Player 2
    if player2_hand[0]['type'] == player2_hand[1]['type'] and player2_hand[0]['type'] == 'attacking':  # two att p2
        p2_attack_score = int(player2_hand[0]['pow_lvl']) + int(player2_hand[1]['pow_lvl'])
        p2_attacking_card_count = 2
    elif player2_hand[0]['type'] == player2_hand[1]['type'] and player2_hand[0]['type'] == 'defending':  # two def p2
        p2_def_score = int(player2_hand[0]['pow_lvl']) + int(player2_hand[1]['pow_lvl'])
        p2_attacking_card_count = 0
    elif player2_hand[0]['type'] != player2_hand[1]['type']:  # one attack/one defend for p2
        p2_attacking_card_count = 1
        if player2_hand[0]['type'] == 'attacking':
            p2_attack_score = int(player2_hand[0]['pow_lvl'])  # sets attacking animal score
            p2_def_score = int(player2_hand[1]['pow_lvl'])  # sets defending animal score
        else:
            p2_def_score = int(player2_hand[0]['pow_lvl'])  # sets defending animal score
            p2_attack_score = int(player2_hand[1]['pow_lvl'])  # sets attacking animal score

    return p1_attack_score, p1_def_score, p2_attack_score, p2_def_score, p1_attacking_card_count, p2_attacking_card_count


def coordinate_score_calc_and_get_round_result(player1_hand, player2_hand):
    """
    Handles calling the proper functions to calculate the winner based on the type of card each player has

    @param player1_hand: player 1's hand
    @type player1_hand: list of dict
    @param player2_hand: player 2's hand
    @type player2_hand: list of dict
    @return: winner, p1_final_score, p2_final_score
    @rtype: tuple
    """
    # should compare players scores
    p1_final_score = p2_final_score = 0

    current_hand_info = get_players_att_and_def_scores_and_type_count(player1_hand, player2_hand)

    p1_attack_score, p1_def_score, p2_attack_score, p2_def_score, p1_attacking_card_count, p2_attacking_card_count = current_hand_info

    # check if both players only have defending cards
    if p1_attacking_card_count == 0 and p2_attacking_card_count == 0:
        winner = both_players_have_only_defending(p1_def_score, p2_def_score, player1_hand,
                                                  player2_hand)
        p1_final_score = p1_def_score
        p2_final_score = p2_def_score

    # check if both players have only attacking animals
    elif p1_attacking_card_count == 2 and p2_attacking_card_count == 2:
        winner = both_players_have_only_attacking(p1_attack_score, p2_attack_score, player1_hand,
                                                  player2_hand)
        p1_final_score = p1_attack_score
        p2_final_score = p2_attack_score

    # handles when one player has 2 attacking and the other has 2 defending (not done, needs testing!!!!!!!!!!!!!!!!!!!!!)
    elif (p1_attacking_card_count == 2 and p2_attacking_card_count == 0) or (
            p1_attacking_card_count == 0 and p2_attacking_card_count == 2):

        p1_final_score = p1_attack_score + p1_def_score
        p2_final_score = p2_attack_score + p2_def_score

        if p1_final_score == 11 or p2_final_score == 11:

            winner = get_winner_2_att_2_def_and_at_least_one_11(p1_final_score, p2_final_score, p1_attacking_card_count,
                                                                p2_attacking_card_count)

        else:  # if neither are equal to 11 than we decide the winner through highest score
            winner = assign_winner_given_final_scores(p1_final_score, p2_final_score)

    # If one player has all attacking and the other has one attacking and one defending.
    # its handled here (not done needs testing working here currently!!!!!!!!!!!11)
    elif (p1_attacking_card_count == 2 and p2_attacking_card_count == 1) or (
            p1_attacking_card_count == 1 and p2_attacking_card_count == 2):

        if p1_attacking_card_count == 2 and p1_attack_score == 11:
            winner = 0  # player 1 winner
            p1_final_score = p1_attack_score
            p2_final_score = p2_attack_score + p2_def_score
        elif p2_attacking_card_count == 2 and p2_attack_score == 11:
            winner = 1  # player 2 winner
            p2_final_score = p2_attack_score
            p1_final_score = p1_attack_score + p1_def_score
        else:
            if p1_attacking_card_count == 2:  # If player 1 has two attacking cards this is true
                p1_attack_score -= p2_def_score
                p1_final_score = p1_attack_score
                p2_final_score = p2_attack_score

            elif p2_attacking_card_count == 2:  # If player 2 has two attacking cards this is true
                p2_attack_score -= p1_def_score
                p2_final_score = p2_attack_score
                p1_final_score = p1_attack_score

            winner = assign_winner_given_final_scores(p1_final_score, p2_final_score)

    # If one player has all defending and the other has one attacking and one defending. its handled here
    elif (p1_attacking_card_count == 0 and p2_attacking_card_count == 1) or (
            p1_attacking_card_count == 1 and p2_attacking_card_count == 0):

        winner, p1_final_score, p2_final_score = one_player_all_def_other_mixed(
            p1_attacking_card_count, p2_attacking_card_count, p1_attack_score, p1_def_score,
            p2_attack_score, p2_def_score)

    else:  # should replace below with better logic i think need to check more closely
        # handles if both players have a mix of types!!!!
        if p1_attacking_card_count == 1:  # If player 1 has defending card
            p2_attack_score -= p1_def_score  # subtract player1 defense
            p2_final_score = p2_attack_score
        if p2_attacking_card_count == 1:  # If player 2 has defending card
            p1_attack_score -= p2_def_score  # subtract player2 defense
            p1_final_score = p1_attack_score

        winner = assign_winner_given_final_scores(p1_final_score, p2_final_score)

    return winner, p1_final_score, p2_final_score


def get_players_highest_valued_card(player1_hand, player2_hand):
    """
    gets highest valued card in each players hand

    @param player1_hand: player 1's hand
    @type player1_hand: list of dict
    @param player2_hand: player 2's hand
    @type player2_hand: list of dict
    @return: int for each players highest valued card
    @rtype: tuple
    """
    if player1_hand[0]['pow_lvl'] > player1_hand[1]['pow_lvl']:
        player1_highest_valued_card = player1_hand[0]['pow_lvl']
    else:
        player1_highest_valued_card = player1_hand[1]['pow_lvl']

    if player2_hand[0]['pow_lvl'] > player2_hand[1]['pow_lvl']:
        player2_highest_valued_card = player2_hand[0]['pow_lvl']
    else:
        player2_highest_valued_card = player2_hand[1]['pow_lvl']

    return int(player1_highest_valued_card), int(player2_highest_valued_card)


def both_players_have_only_defending(player1_defense_score, player2_defense_score, player1_hand, player2_hand):
    """
    handles the rules for when both players have only defending

    @param player1_defense_score:
    @type player1_defense_score: int
    @param player2_defense_score:
    @type player2_defense_score: int
    @param player1_hand:
    @type player1_hand: list of dict
    @param player2_hand:
    @type player2_hand: list of dict
    @return: winner:
    @rtype: int
    """
    winner = 2  # draw
    if player1_defense_score == 11 and player2_defense_score == 11:
        player1_highest_value, player2_highest_value = get_players_highest_valued_card(player1_hand, player2_hand)
        if player1_highest_value > player2_highest_value:
            winner = 0  # player 1 winner
        elif player2_highest_value > player1_highest_value:
            winner = 1  # player 2 winner
    elif player1_defense_score == 11:
        winner = 0  # player 1 winner
    elif player2_defense_score == 11:
        winner = 1  # player 2 winner

    # don't need else for draw here since winner is set to 2 at the beginning
    return winner


def both_players_have_only_attacking(player1_attack_score, player2_attack_score, player1_hand, player2_hand):
    """
    handles the rules for when both players have only attacking

    @param player1_attack_score:
    @type player1_attack_score: int
    @param player2_attack_score:
    @type player2_attack_score: int
    @param player1_hand:
    @type player1_hand: list of dict
    @param player2_hand:
    @type player2_hand: list of dict
    @return:
    @rtype:
    """
    winner = 2  # draw
    if player1_attack_score == 11 and player2_attack_score == 11:
        player1_highest_value, player2_highest_value = get_players_highest_valued_card(player1_hand, player2_hand)
        if player1_highest_value > player2_highest_value:
            winner = 0  # player 1 winner
        elif player2_highest_value > player1_highest_value:
            winner = 1  # player 2 winner
    elif player1_attack_score == 11:
        winner = 0  # player 1 winner
    elif player2_attack_score == 11:
        winner = 1  # player 2 winner
    else:
        if player1_attack_score > player2_attack_score:
            winner = 0
        elif player2_attack_score > player1_attack_score:
            winner = 1

    # don't need else for draw here since winner is set to 2 at the beginning
    return winner


def get_winner_2_att_2_def_and_at_least_one_11(p1_final_score, p2_final_score, p1_attacking_card_count, p2_attacking_card_count):
    """
    gets winner when at least one player has 2 att or 2 def and 11 and The other player will have the opposite of the
    first player so 2 def or 2 attack and may have 11 as well

    @param p1_final_score: player1 final score
    @type p1_final_score: int
    @param p2_final_score: player2 final score
    @type p2_final_score: int
    @param p1_attacking_card_count: player 1 attacking card count
    @type p1_attacking_card_count: int
    @param p2_attacking_card_count: player 2 attacking card count
    @type p2_attacking_card_count: int
    @return: winner (2 == draw, 1 == player 2 win, 2 == player 1 win)
    @rtype: int
    """
    winner = 2
    if (p1_attacking_card_count == 2 and p1_final_score == 11 and p2_final_score != 11) or (
            p1_attacking_card_count == 0 and p1_final_score == 11 and p2_final_score != 11):
        # player 1 has 2 attacking or 2 defending with a total score of 11. player 2 has 2 def or 2 attack != 11
        winner = 0  # player 1 winner
    elif (p2_attacking_card_count == 2 and p2_final_score == 11 and p1_final_score != 11) or (
            p2_attacking_card_count == 0 and p2_final_score == 11 and p1_final_score != 11):
        # player 2 has 2 attacking or 2 defending with a total score of 11. player 1 has 2 def or 2 attack != 11
        winner = 1  # player 2 winner
    elif (p2_attacking_card_count == 2 and p2_final_score == 11 and p1_final_score == 11) or (
            p2_attacking_card_count == 0 and p2_final_score == 11 and p1_final_score == 11):
        # player 2 has 2 attacking or 2 defending with a total score of 11. player 1 has 2 def or 2 attack == 11
        if p2_attacking_card_count == 2:
            winner = 0  # player 1 winner
        elif p2_attacking_card_count == 0:
            winner = 1  # player 2 winner

    return winner


def one_player_all_def_other_mixed(p1_attacking_card_count, p2_attacking_card_count, p1_attack_score, p1_def_score,
                                   p2_attack_score, p2_def_score):
    """
    Handles rules/getting results for both players having 1 attacking and 1 defending

    @param p1_attacking_card_count: holds count of players current attacking cards in hand
    @type p1_attacking_card_count: int
    @param p2_attacking_card_count: holds count of players current attacking cards in hand
    @type p2_attacking_card_count: int
    @param p1_attack_score: current attacking score
    @type p1_attack_score: int
    @param p1_def_score: current attacking score
    @type p1_def_score: int
    @param p2_attack_score:
    @type p2_attack_score: int
    @param p2_def_score:
    @type p2_def_score: int
    @return:  winner, p1_final_score, p2_final_score
    @rtype: list
    """
    winner = 2
    p1_final_score = p2_final_score = 0

    if p1_attacking_card_count == 0 and p1_attack_score == 11:
        winner = 0  # player 1 winner
        p1_final_score = p1_def_score
        p2_final_score = p2_attack_score + p2_def_score
    elif p2_attacking_card_count == 0 and p2_attack_score == 11:
        winner = 1  # player 2 winner
        p2_final_score = p2_def_score
        p1_final_score = p1_attack_score + p1_def_score
    else:
        if p1_attacking_card_count == 0:  # If player 1 has two attacking cards this is true
            p2_attack_score -= p1_def_score
            p2_final_score = p2_attack_score

        elif p2_attack_score == 0:  # If player 2 has two attacking cards this is true
            p1_attack_score -= p2_def_score
            p1_final_score = p1_attack_score

        if p1_final_score >= 0:
            winner = 0  # player 1 winner
        elif p2_final_score >= 0:
            winner = 1  # player 2 winner

    return winner, p1_final_score, p2_final_score


def assign_winner_given_final_scores(player1_final_score, player2_final_score):
    """
    Used to find winner when only final scores are needed. used to reduce repeated code

    @param player1_final_score:
    @type player1_final_score: int
    @param player2_final_score:
    @type player2_final_score: int
    @return: winner: 2 if draw, 1 for player 2, and 0 for player 1
    @rtype: int
    """
    winner = 2
    if player1_final_score > player2_final_score:
        winner = 0  # player 1 winner
    elif player2_final_score > player1_final_score:
        winner = 1  # player 2 winner
    # don't need else to set winner to 2 because it is set to 2 at the top

    return winner
