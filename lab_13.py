#lab_13
#game: Farkle
#group members: Kendall Starcevich, Tyler Nansel, Xavier Washington
#how to play:
"""Farkle is a two-player game played with six dice and rolling all six at the same time. After seeing all the dice that were rolled,
set the ones with melds to the side. Melds are explained down below. They can set aside any melds they want for points, or they may
roll again. If they do not roll again then they may get the points for the meld they wanted which is called a bank. After you bank
it is the next person's turn. If they roll again and they get no melds in that roll they farkled which means they lost all points
in that turn. Melds do not stack, if you get two ones that are worth two hundred points for that turn. If you roll the next turn
and get another one, that is worth 100 points. Whoever has the most points at the end of the round wins!
 
Melds, Ones are worth 100 points, fives are worth 50 points, a set with three ones are worth 1,000 points, three twos are worth
200 points, three threes are worth 300, Three fours are worth 400, Three fives are worth 500, Three sixes are worth 600, Four
of any number are worth 1,000 points, Five of any number are worth 2,000 points, Six of any number are worth 3,000 points. A run,
which is rolling an order of 1,2,3,4,5,6 is worth 2,500 points"""

#criteria met: at least 1 list, for loop, nested if-statement, nested for loop, at least 2 functions other than roll_die

def print_rules():
    print("Here are the rules, have fun!:")
    print("Farkle is a two-player game played with six dice and rolling all six at the same time. After seeing all the dice that were rolled,")
    print("set the ones with melds to the side. Melds are explained down below. They can set aside any melds they want for points, or they may")
    print("roll again. If they do not roll again then they may get the points for the meld they wanted which is called a bank. After you bank")
    print("it is the next person's turn. If they roll again and they get no melds in that roll they farkled which means they lost all points")
    print("in that turn. Melds do not stack, if you get two ones that are worth two hundred points for that turn. If you roll the next turn")
    print("and get another one, that is worth 100 points. Whoever has the most points at the end of the round wins!")
    print("and get another one, that is worth 100 points. Whoever has the most points at the end of the round wins!")
    print("Melds, Ones are worth 100 points, fives are worth 50 points, a set with three ones are worth 1,000 points, three twos are worth")
    print("200 points, three threes are worth 300, Three fours are worth 400, Three fives are worth 500, Three sixes are worth 600, Four")
    print("of any number are worth 1,000 points, Five of any number are worth 2,000 points, Six of any number are worth 3,000 points. A run,")
    print("which is rolling an order of 1,2,3,4,5,6 is worth 2,500 points")
    
"""
Will print out the directions of Farkle

Parameters:
    none
    
Return:
    12 lines of strings explaining the rules to Farkle
"""
user_answer=input("Do you know how to play Farkle? (yes or no):")
if user_answer=="yes":
        print("Have fun!")
if user_answer=="no":
        print_rules()
        

P1=(input("Player 1 name: "))
P2=(input("Player 2 name: "))
import random
def roll_die(num_sides=6):
    """
    Will return a random number between 1 and num_sides, as a dice would.
    
    Parameters:
        num_sides: the upper bound on the random number
    Return:
        a random number between 1 and num_sides, inclusive.
    """
    return random.randint(1,num_sides)
p1_roll = []
p2_roll = []

for x in range(6):
    p1_roll.append(roll_die(6))
    p2_roll.append(roll_die(6))
print(P1, "rolled", p1_roll)
print(P2, "rolled",p2_roll)
"""
    Will return the score that the selected player has earned.
    
    Parameters:
        roll: represents rolling the dice
        
    Return:
        a score based on which numbers are rolled
        
"""
  

def scoring(roll):
    score = 0
    num1 = 0
    num2 = 0
    num3 = 0
    num4 = 0
    num5 = 0
    num6 = 0
    for x in roll :
        if x == 1 :
           score +=100
           num1 += 1
        elif x == 2 :
            num2 +=1
        elif x == 3 :
            num3 +=1
        elif x == 4 :
            num4 +=1
        elif x == 5 :
            score += 50
            num5 += 1
        elif x == 6 :
            num6 +=1
    if num1 == 3:
        score +=700
    if num2 == 3:
        score +=200
    if num3 == 3:
        score +=300
    if num4 == 3:
        score +=400
    if num5 == 3:
        score += 350
    if num6 == 3:
        score += 600
       
        
    if num1 == 4:
        score +=1000
    if num2 == 4:
        score +=1000
    if num3 == 4:
        score +=1000
    if num4 == 4:
        score +=1000
    if num5 == 4:
        score +=1000
    if num6 == 4:
        score +=1000
   
    
    if num1 == 5:
        score +=2000
    if num2 == 5:
        score +=2000
    if num3 == 5:
        score +=2000
    if num4 == 5:
        score +=2000
    if num5 == 5:
        score +=2000
    if num6 == 5:
        score +=2000
       
    
    if num1 == 6:
        score +=3000
    if num2 == 6:
        score +=3000
    if num3 == 6:
        score +=3000
    if num4 == 6:
        score +=3000
    if num5 == 6:
        score +=3000
    if num6 == 6:
        score +=3000
   
    
    if roll == [1,2,3,4,5,6]:
        score += 2350
 
 
    return score


print(P1,"earned",scoring(p1_roll), "points")
print(P2,"earned",scoring(p2_roll), "points")

if scoring(p1_roll)> scoring(p2_roll):
    print("so...", P1, "wins!")
if scoring(p1_roll)< scoring(p2_roll):
    print("so...",P2, "wins!")
if scoring(p1_roll)== scoring(p2_roll):
    print("It's a tie!")


    


