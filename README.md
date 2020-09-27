

# Magical Animals
A command line based card game designed for two players. With the
ability to save your game results you can easily track how many times you’re victorious!!!
Currently the game has one set of 20 animals to battle with.

*To run game!!*
**python3 main.py**

**Current animals available in the game**

![animal_names](https://user-images.githubusercontent.com/17306905/94356147-0f142580-0059-11eb-8289-d3e8584b8a5b.png)


# Game information (Rules below)

There are two players and a deck of 20 cards. The cards are divided into two groups. 

**The first group is attacking animals. They are:**

__1. Cat
2. Eagle
__3. Liger
4. Sea Serpent
__5. Gargoyle
6. Hydra
__7. Vampire
8. Giant
__9. Werewolf
10. Dragon__

**The second group is defending animals. They are:

**1. Dog
2. Owl
**3. Gnome
4. Mermaid
**5. Fairy
6. Centaur
**7. Hippogriff
8. Sphinx
**9. Gryphon
10 Unicorn**

## The number next to each animal represents it's attacking or defending strength.

To start, both players are dealt two cards from a shuffled deck of magical animal cards. 

# The rules are as follows.

If both players have defending animals, the game is a draw.
If both players have attacking animals, the player whose animals have the higher total score wins.
If one player has two attacking animals and the other has defending animals, then the player with the higher animal sum wins (Unicorn + Gryphon = 19 beats Hydra + Vampire = 13)
If both players have one attacking animal and one defending animal, the player that delivers more damage wins. (Unicorn protects against 10 damage points and Giant delivers 8. This beats a Werewolf and a Hippogriff because the 9 attacking points are stopped by the Unicorn and the 7 defense points aren't enough to stop the Giant).
If one player has two attacking animals and the other has one attacking animal and one defending animal, then the defending animal's score is subtracted from the sum of the two attacking animals and the player with the higher remaining attacking score wins.
If one player has two defending animals and the other has one attacking animal and one defending animal, then the sum of the defending animals is subtracted from the attacking animal. If the number is positive, the attacker wins, if it is negative, the defender wins.
If either player has two attacking or two defending cards that total to 11 points, that player wins (for example: Dog + Unicorn = 11 and Eagle + Werewolf = 11). If both players have an 11 the victor is the defender. If both players have only defensive or attacking cards equaling 11, the victor is the player with the highest card.
All cards are dealt on the table face up so the players can see one each other's cards.
After the two cards are dealt to both players can decide to trade a card. The players must choose which card to trade and the cards will be dealt without them seeing the other player's new card. That is to say, both players decide to trade a card and what card to trade in advance of seeing the other player's new card. Both new cards are revealed at the same time.
The game must write to an external file the number of wins for each of the players and the number of draws. The score should be loaded at the start of the game and written back to the file after each round. This file must not be overwritten each time the game is played so that over many runs of the program we can see which player is doing better. This is what a sample game might look like:
