class PlayingCard:
    
    def __init__(self,v,s):
        if (type(v) != int) or v>14 or v<2:
            raise Exception("A PlayingCard's value must be an integer in the range 2-14.")
        self.__value = v
        self.__suit = s

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

print("Here's what the card looks like:",seven_of_spades)
if (seven_of_spades<ten_of_hearts):
    print("Player 2 wins the hand!")
elif seven_of_spades==ten_of_hearts:
    print("It's a tie!")
else:
    print("Player 1 wins the hand!")



class Deck:

    def __init__(self):
        self.__card_list=[]

    def __repr__(self):
        return str(self.__card_list)
    
    def put_card_on_top(self, new_card):
        self.__card_list.append(new_card)
    
    def remove_from_top(self):
        return self.__card_list.pop()
    
    def is_empty(self):
        if len(self.__card_list)==0:
            return True
        else:
            return False
        
    def shuffle(self): #fix this 
        import random
        return random.shuffle(self.__card_list)

my_deck=Deck()
#print(my_deck)
two_of_clubs = PlayingCard(2,"♣")
two_of_hearts = PlayingCard(2,"♡")
ten_of_hearts = PlayingCard(10,"♡")
seven_of_spades = PlayingCard(7,"♠")
four_of_diamonds = PlayingCard(4,"♢")

my_deck.put_card_on_top(two_of_clubs)
my_deck.put_card_on_top(two_of_hearts)
my_deck.put_card_on_top(ten_of_hearts)
my_deck.put_card_on_top(seven_of_spades)

print(my_deck)

print(my_deck.remove_from_top())
print(my_deck)
print(my_deck.is_empty())
#print(my_deck.shuffle)