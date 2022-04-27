
print("Keep in mind that the format is:")
print("1|2|3")
print("-+-+-")
print("4|5|6")
print("-+-+-")
print("7|8|9")
print()

Board = {'1': ' ' , '2': ' ' , '3': ' ' ,
         '4': ' ' , '5': ' ' , '6': ' ' ,
         '7': ' ' , '8': ' ' , '9': ' ' }

board_keys = []
for key in Board:
    board_keys.append(key)

def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


def main():

    turn = 'X'
    count = 0


    for i in range(10):
        printBoard(Board)
        print(f"It's your turn {turn}.")

        move = input()        

        if Board[move] == " ":
            Board[move] = turn
            count += 1
        else:
            print("is already filled.\nMove to which place?")
            continue

        
        if count >= 5:
            if Board["1"] == Board["2"] == Board["3"] != " ": 
                printBoard(Board)                
                print(f" congratulations {turn} won.") 
                print("Thanks for playing.")               
                break
            elif Board["4"] == Board["5"] == Board["6"] != " ": 
                printBoard(Board)
                print(f" congratulations {turn} won.") 
                print("Thanks for playing.")    
                break
            elif Board["7"] == Board["8"] == Board["9"] != " ": 
                printBoard(Board)
                print(f" congratulations {turn} won.") 
                print("Thanks for playing.")   
                break
            elif Board["1"] == Board["4"] == Board["7"] != " ": 
                printBoard(Board)
                print(f" congratulations {turn} won.") 
                print("Thanks for playing.")   
                break
            elif Board["2"] == Board["5"] == Board["8"] != " ": 
                printBoard(Board)
                print(f" congratulations {turn} won.") 
                print("Thanks for playing.")   
                break
            elif Board["3"] == Board["6"] == Board["9"] != " ": 
                printBoard(Board)
                print(f" congratulations {turn} won.") 
                print("Thanks for playing.")   
                break 
            elif Board["7"] == Board["5"] == Board["3"] != " ": 
                printBoard(Board)
                print(f" congratulations {turn} won.") 
                print("Thanks for playing.")    
                break
            elif Board["1"] == Board["5"] == Board["9"] != " ": 
                printBoard(Board)
                print(f" congratulations {turn} won.") 
                print("Thanks for playing.")    
                break 

        if count == 9:
            print("Thanks for playing.")                
            print("It's a Tie!!")

        if turn =="X":
            turn = "O"
        else:
            turn = "X"    


    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            Board[key] = " "

        


if __name__ == "__main__":
    main()


    