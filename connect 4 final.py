import numpy as np
import turtle
t= turtle.Turtle()

print("Welcome to our Connect 4! The objective of the game is for one of the two players to make either a straight vertical, straight horizontal, or diagonal line with their colored piece to win!")
print("You as the player have the option to place your piece in any column(1-7) that does not already have a piece. Now that you are aware of the rules, let's begin!!!")
column = np.array([0,0,0,0,0,0])
game_board = []

for i in range(7):
    game_board.append(np.array(column))

def PlacePiece(team, position):
    """
    try: places piece for each team by 
    categorizing as positive or negative 1. Places the piece on the board.
    Except: If there is too many pieces in one column, then it will
    print column overflow, giving another change for the individual to put their piece elsewhere.
    """
    position -= 1
    
    try:
        lastIndex =  np.argwhere(game_board[position] == 0)[-1]
        game_board[position][lastIndex] = team
    
    except:
        print("Column overflow!")
        game_board[position][0] = team


def CheckHorizontal(column, row):   
    
    """
    Checks to see if there was a horizontal connect 7
    will go to function check for winners to verify the win!
    """
    
    try:
        team = game_board[column][row]
        nextPiece = game_board[column+1][row]
        nextPiece2 = game_board[column+2][row]
        nextPiece3 = game_board[column+3][row]
        
        if((team * 4) == (team+nextPiece+nextPiece2+nextPiece3)):
            return True
        else:
            return False   
    except:
        return False
        pass
     
    

def CheckVertical(column, row):
    """
    Checks to see if there was a vertical connect 7
    will go to function check for winners to verify the win!
    """
    try:
        team = game_board[column][row]
        nextPiece = game_board[column][row+1]
        nextPiece2 = game_board[column][row+2]
        nextPiece3 = game_board[column][row+3]
        
        if((team * 4) == (team+nextPiece+nextPiece2+nextPiece3)):
            return True
        else:
            return False   
    except:
        return False
        pass 

def CheckDiagnalRight(column, row):
    """
    Checks to see if there was a diagonal connect 7 going to the right 
    will go to function check for winners to verify the win!
    """
    try:
        team = game_board[column][row]
        nextPiece = game_board[column+1][row+1]
        nextPiece2 = game_board[column+2][row+2]
        nextPiece3 = game_board[column+3][row+3]
        
        if((team * 4) == (team+nextPiece+nextPiece2+nextPiece3)):
            return True
        else:
            return False   
    except:
        return False
        pass
    
def CheckDiagnalLeft(column, row):
    """
    Checks to see if there was a diagonal connect 7 going to the left
    will go to function check for winners to verify the win!
    """
    try:
        team = game_board[column][row]
        nextPiece = game_board[column+1][row-1]
        nextPiece2 = game_board[column+2][row-2]
        nextPiece3 = game_board[column+3][row-3]
        
        if((team * 4) == (team+nextPiece+nextPiece2+nextPiece3)):
            return True
        else:
            return False   
    except:
        return False
        pass  



def CheckForWinners(team):
    """
    Verifies the winner by going through function check horizontal,
    checkvertical, checkdiagonalright, and checkdiagonalleft to find 
    which way the player won.
    """
    for i in range(len(game_board)):
        for j in range(len(game_board[0])):         
            if(game_board[i][j] == team):
                is_winner = False
                is_winner |= CheckHorizontal(i,j)
                is_winner |= CheckVertical(i,j)
                is_winner |= CheckDiagnalRight(i,j)
                is_winner |= CheckDiagnalLeft(i,j)
                if(is_winner):
                    return True
                
    return False
        
        
def PrintGameBoard():
    """
    Function for printing the game board with the updated pieces in their wanted spots.
    Used to print the board after each participant has taken a turn
    """
    r = 40
    t.speed(0)
    seperation = 20
    t.pencolor()
    
    for i in range(len(game_board[0])):
        # printstr = ""
        for j in range(len(game_board)):
            t.penup()
            position = game_board[6-j][5-i]
            if position==1:
                t.pencolor('red')
            elif position==-1:
                t.pencolor('yellow')
            else:
                t.pencolor('blue')
         
            xPosition = ((6-j)*(seperation + (2 * r))) - 300
            yPosition = (i*(seperation + (2 * r))) -250
            t.goto(xPosition, yPosition)     
            t.pendown()
            t.circle(r)
            
activePlayer = 1

turtle.clear()
turtle.reset()
t.pensize(23)
while True:
    try:
        position = int(input("Which column will you place your token in:\n"))
        if (position <=0 or position >7) or (int(position)!=position):
            print("Bad input, please try a integer between 1 and 7!")
        else:
            PlacePiece(activePlayer,position)
            winner = CheckForWinners(activePlayer)
            PrintGameBoard()
            if(winner):
                if activePlayer==-1:
                    activePlayer=2
                print(f" player {activePlayer} has won!")
                break
            activePlayer *= -1
    except ValueError:
        print("Bad input, please try a integer between 1 and 7!")

