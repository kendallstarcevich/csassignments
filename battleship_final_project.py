#CS-65 Final Project
#"Battleship" game
#group members: Tyler Nansel and Kendall Starcevich
import random
board = []

for i in range(7):
    board.append([" "] * 8) #can change to any symbol
  
def print_board(board):
    print(" ","1","2","3","4","5","6","7")
    counter=1
    for row in board:
        print( counter," ".join(row))
        counter+=1
    """
    This function prints the Battleship board that will be used to play the game.
    
    Parameters: board: (list) list of rows and columns used to print the board
    
    Returns: Printed board
    
    """
      
def start_game():
    print ("Let's play Battleship!")
    """
    This function introduces the game.
    
    Parameters: none
    
    Returns: greeting (string): Let's play battleship!
    """
  
def opening ():
    x = input("Do you know how to play Battleship? (yes or no):")
    x = x.lower()
    if x == "yes" :
        print (" This version uses 2 ships that are 1 character big each. Good luck! ")
    else :
        print (" Battleship is a game of hide and seek, hide your ships, then race to find the enemys ships before they find yours. Simple enough, good luck!")
    input("Start?:",)
    """
    This function introduces the game. It asks the player if they know the rules, and if not, it explains them.
    
    Paramaters: none
    
    Returns: if the player knows how to play: (str) short good luck message
             if the player does not know how to play: (str) quick explanation of the rules and good luck message
    """
   
def user_ship_placement ():
    ship1X = input("Input your first ships X cordinate (1-7):",)
    ship1Y = input("Input your first ships Y cordinate(1-7):",)
    ship2X = input("Input your second ships X cordinate:(1-7)",)
    ship2Y = input("Input your second ships Y cordinate:(1-7)",)
    print("Your ships are at" ,ship1X,",",ship1Y, "and" ,ship2X,",",ship2Y)
    return ship1X, ship1Y, ship2X, ship2Y

"""
This function places the users ships to make game-play realistic to a traditional battle ship game.

Parameters: none

Returns: an x and y coordinate for each ship that the user input
"""
 
CPUship1X = random.randint(0,6)
CPUship1Y = random.randint(0,6)
CPUship2X = random.randint(0,6)
CPUship2Y = random.randint(0,6)

def test_CPUships():
    print("*test* The CPU ships are at:")
    print(CPUship1X+1, ",",CPUship1Y+1)
    print(CPUship2X, ",", CPUship2Y)
    
"""
This function is used to test the location of the CPU ships to make sure the program is running correctly.

Parameters: none

Returns: Coordinates of the location of 2 CPU ships
"""

  
start_game ()
opening ()
print_board(board)
user_ship_placement()
sunk_ships = 0
#test_CPUships()

for turn in range(8):
    guess_row = int(input("Guess Row(1-7):"))
    guess_col = int(input("Guess Col:(1-7)"))
   
    a = random.randint(0,49)
    b = random.randint(0,2)
    if a == 1 and b == 1:
        print ("Oh no! You lost. But you can keep guessing if you like.")
 
    # if the user's right, the game ends
    if guess_row == CPUship1X+1  and guess_col == CPUship1Y+1:
        print( "Congratulations! You sunk my battleship!")
        sunk_ships += 1
   
    elif guess_row == CPUship2X and guess_col == CPUship2Y:
        print( "Congratulations! You sunk my battleship!")
        sunk_ships += 1
    elif sunk_ships == 2:
        print ("Game Over, you win!!")
        break
       
    else:
        #warning if the guess is out of the board
        if (guess_row < 1 or guess_row > 7) or (guess_col < 1 or guess_col > 7):
            print ("Oops, that's not even in the ocean.")
      
        #warning if the guess was already made
        elif(board[guess_row-1][guess_col-1] == "X" ):
            print ("You guessed that one already.")
      
        #if the guess is wrong, mark the point with an X and start again
        else:
            print ("You missed my battleship!")
            board[guess_row-1][(guess_col)-1] = "X"
      
        # Print turn and board again here
        print ("Turn " + str(turn+1) + " out of 8." )
        print_board(board)
 
#if the user have made 8 tries, it's game over
if turn >= 7:
    print( "Game Over, you lost :(")
