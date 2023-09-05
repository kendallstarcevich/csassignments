"""
I am doing option 1.
I implemented a new rule that made it much harder to tie in a round. If the number values were the same, I then moved to suits. In my "suit_points" function, I made a heart worth 4 points, a diamond
worth 3, spade worth 2, and clubs worth 1. The only way to get a tie then in the round was to have the exact same number and suit. Here is a sample run:
(you can see my changes implemented in lines 23 and 57 where the numbers are the same and the points have to be resorted to the faces)

Here's the pre-shuffled deck: [2♠, 3♠, 4♠, 5♠, 6♠, 7♠, 8♠, 9♠, 10♠, 11♠, 12♠, 13♠, 14♠, 2♣, 3♣, 4♣, 5♣, 6♣, 7♣, 8♣, 9♣, 10♣, 11♣, 12♣, 13♣, 14♣, 2♡, 3♡, 4♡, 5♡, 6♡, 7♡, 8♡, 9♡, 10♡, 11♡, 12♡, 13♡, 14♡, 2♢, 3♢, 4♢, 5♢, 6♢, 7♢, 8♢, 9♢, 10♢, 11♢, 12♢, 13♢, 14♢]
Here's the deck after the shuffle: [3♢, 10♢, 11♠, 11♣, 3♣, 14♠, 5♡, 6♢, 5♢, 13♡, 4♣, 3♡, 7♣, 5♣, 11♢, 9♣, 6♣, 2♠, 12♣, 5♠, 7♠, 8♡, 8♣, 6♡, 7♡, 12♢, 4♠, 11♡, 4♡, 14♡, 4♢, 13♣, 7♢, 2♡, 2♢, 10♡, 12♠, 12♡, 13♠, 10♠, 3♠, 10♣, 9♢, 6♠, 9♡, 2♣, 8♠, 14♢, 9♠, 13♢, 8♢, 14♣]
Player 1: 14♣ , Player 2: 8♢
Player 1 wins this hand.
Player 1: 13♢ , Player 2: 9♠
Player 1 wins this hand.
Player 1: 14♢ , Player 2: 8♠
Player 1 wins this hand.
Player 1: 2♣ , Player 2: 9♡
Player 2 wins this hand.
Player 1: 6♠ , Player 2: 9♢
Player 2 wins this hand.
Player 1: 10♣ , Player 2: 3♠
Player 1 wins this hand.
Player 1: 10♠ , Player 2: 13♠
Player 2 wins this hand.
Player 1: 12♡ , Player 2: 12♠
Player 1 wins this hand.
Player 1: 10♡ , Player 2: 2♢
Player 1 wins this hand.
Player 1: 2♡ , Player 2: 7♢
Player 2 wins this hand.
Player 1: 13♣ , Player 2: 4♢
Player 1 wins this hand.
Player 1: 14♡ , Player 2: 4♡
Player 1 wins this hand.
Player 1: 11♡ , Player 2: 4♠
Player 1 wins this hand.
Player 1: 12♢ , Player 2: 7♡
Player 1 wins this hand.
Player 1: 6♡ , Player 2: 8♣
Player 2 wins this hand.
Player 1: 8♡ , Player 2: 7♠
Player 1 wins this hand.
Player 1: 5♠ , Player 2: 12♣
Player 2 wins this hand.
Player 1: 2♠ , Player 2: 6♣
Player 2 wins this hand.
Player 1: 9♣ , Player 2: 11♢
Player 2 wins this hand.
Player 1: 5♣ , Player 2: 7♣
Player 2 wins this hand.
Player 1: 3♡ , Player 2: 4♣
Player 2 wins this hand.
Player 1: 13♡ , Player 2: 5♢
Player 1 wins this hand.
Player 1: 6♢ , Player 2: 5♡
Player 1 wins this hand.
Player 1: 14♠ , Player 2: 3♣
Player 1 wins this hand.
Player 1: 11♣ , Player 2: 11♠
Player 2 wins this hand.
Player 1: 10♢ , Player 2: 3♢
Player 1 wins this hand.
Player 1 score: 15 , Player 2 score: 11
Player 1 wins the game!!!

"""
class PlayingCard:
    
    def __init__(self,v,s):
        if (type(v) != int) or v>14 or v<2:
            raise Exception("A PlayingCard's value must be an integer in the range 2-14.")
        self.__value = v
        self.__suit = s
        self.suit_points()
        
    def suit_points(self):
    
        if self.__suit == "♡":
            self.points=4
        elif self.__suit=="♢":
            self.points=3
        elif self.__suit=="♠":
            self.points=2
        elif self.__suit=="♣":
            self.points=1


    def face(self):
        if self.__value == 11:
            return "J"
        elif self.__value== 12:
            return "Q"
        elif self.__value==13:
            return "K"
        elif self.__value==14: #or self._value==1:
            return "A"
        else: 
            return str(self.__value)
        
    def __lt__(self, other):
        if (self.__value< other.__value):
            return True
        elif self.__value==other.__value:
            return self.points < other.points
        else:
            return False
    
    def __eq__(self, other):
        if (self.__value== other.__value):
            return True
        else:
            return False
    
    def __repr__(self):
        return str(self.__value) + str(self.__suit)
        
two_of_clubs = PlayingCard(2,"♣")
two_of_hearts = PlayingCard(2,"♡")
ten_of_hearts = PlayingCard(10,"♡")
seven_of_spades = PlayingCard(7,"♠")
four_of_diamonds = PlayingCard(4,"♢")
#pokemon=PlayingCard("Pikachu", 14) #example to test exception

#print("Here's what the card looks like:",seven_of_spades)
"""
if (seven_of_spades<ten_of_hearts):
    print("Player 2 wins the hand!")
elif seven_of_spades==ten_of_hearts:
    print("It's a tie!")
else:
    print("Player 1 wins the hand!")
"""


class Deck:

    def __init__(self):
        self.__card_list=[]

    def __repr__(self):
        return str(self.__card_list)
    
    def put_on_top(self, new_card):
        self.__card_list.append(new_card)
    
    def remove_from_top(self):
        return self.__card_list.pop()
    
    def is_empty(self):
        if len(self.__card_list)==0:
            return True
        else:
            return False
        
    def shuffle(self): 
        import random
        random.shuffle(self.__card_list)

my_deck=Deck()
#print(my_deck)
two_of_clubs = PlayingCard(2,"♣")
two_of_hearts = PlayingCard(2,"♡")
ten_of_hearts = PlayingCard(10,"♡")
seven_of_spades = PlayingCard(7,"♠")
four_of_diamonds = PlayingCard(4,"♢")


high_card_deck = Deck()

#create each of the 52 playing cards and put them in the deck
suits = ["♠","♣","♡","♢"]
for s in suits:
    for v in range(2,15):
        curr_card = PlayingCard(v,s)
        high_card_deck.put_on_top(curr_card)
        
#look at the deck both before and after shuffling        
print("Here's the pre-shuffled deck:",high_card_deck)
high_card_deck.shuffle()
print("Here's the deck after the shuffle:",high_card_deck)

#initialize both player's scores to 0
p1score = 0
p2score = 0

#keep going until all cards are dealt out
while not high_card_deck.is_empty():
    
    #draw a card for each player
    p1card = high_card_deck.remove_from_top()
    p2card = high_card_deck.remove_from_top()
    
    print("Player 1:",p1card,", Player 2:",p2card)


    if p1card > p2card:
        p1score += 1
        print("Player 1 wins this hand.")
    elif p1card < p2card:
        p2score += 1
        print("Player 2 wins this hand.")
    else:
        print("This hand is a draw.")
        
        
#Figure out who wins and display the game-end message
print("Player 1 score:",p1score,", Player 2 score:",p2score) 
if p1score > p2score:
    print("Player 1 wins the game!!!")
elif p2score > p1score:
    print("Player 2 wins the game!!!")
else:
    print("The game is a tie :(")
