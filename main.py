
def printBoard(xState, zState):
    print("")
    zero = 'X' if xState[0] else ('O' if zState[0] else 0)
    one = 'X' if xState[1] else ('O' if zState[1] else 1)
    two = 'X' if xState[2] else ('O' if zState[2] else 2)
    three = 'X' if xState[3] else ('O' if zState[3] else 3)
    four = 'X' if xState[4] else ('O' if zState[4] else 4)
    five = 'X' if xState[5] else ('O' if zState[5] else 5)
    six = 'X' if xState[6] else ('O' if zState[6] else 6)
    seven = 'X' if xState[7] else ('O' if zState[7] else 7)
    eight = 'X' if xState[8] else ('O' if zState[8] else 8)
    print(f" {zero} | {one} | {two} ")
    print(f"---|---|---")
    print(f" {three} | {four} | {five} ")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight} ")
    

def checkWinner(xState, zState):
    winningCombinations = [
        [0, 1, 2],[3, 4, 5],[6, 7, 8],   # rows
        [0, 3, 6],[1, 4, 7],[2, 5, 8],   #columns
        [0, 4, 8],[2, 4, 6]       #diagonals
    ]   

    for combination in winningCombinations:
        if(all(xState[i] == 1 for i in combination)):
            print("X Wins")
            return 'X'
        if(all(zState[i] == 1 for i in combination)):
            print("O Wins")
            return 'O'


if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    print("Welcome to Tic Tac Toe.")
    turn = 1 # if turn is assigned to 1 it means X turn. If it is assigned to 0 then O turn
    printBoard(xState, zState)
    while(True):
        if(turn == 1):
            print("Turn = X")
            value = int(input("Please enter a Value: "))
            if(xState[value] == 0 and zState[value] == 0):
                xState[value] = 1
                printBoard(xState, zState)
                turn = 0
                win = checkWinner(xState, zState)
                if(win == 'X'):
                    break
            else:
                print("Invalid Move! Please Try Again")    

        else:
            print("Turn = O")
            value = int(input("Please enter a Value: "))
            if(xState[value] == 0 and zState[value] == 0):
                zState[value] = 1    
                printBoard(xState, zState)
                turn = 1
                win = checkWinner(xState, zState)
                if(win == 'O'):
                    break
            else:
                print("Invalid Move! Please Try Again")    
            
        