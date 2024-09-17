import random 

#title for page
print(' ')
print('===================')
print('ROCK PAPER SCISSORS')
print('===================')
print(' ')
#assigned variables
Rock = 1
Paper = 2
Scissors = 3

#print statement for options to pick from
print('1) Rock')
print('2) Paper')
print('3) Scissors')

#set my player 1 and player 2
player1 = int(input('Player one pick a number: '))
player2 = int(input('Player two pick a number: '))

#creates space
print(' ')
#prints the input
print('Player One Choose: ' + str(player1))
print('Player Two Choose: ' + str(player2))

#if statement for playing the game
if player1 > Rock and player2 < Scissors:
    print('Player One wins')
elif player1 > Scissors and player2 <= Paper:
    print('Player One wins')
elif player1 > Paper and player2 <= Rock:
    print('Player One wins')
else :
    print('Player Two Wins')

#if statement for if player 1 and player 2 gets a tie   
if player1 == Rock and player2 == Rock:
    print("It's a tie")
elif player1 == Scissors and player2 == Scissors:
    print("It's a tie")
elif player1 == Paper and player2 == Paper:
    print("It's a tie")
else:
    pass

while True:

    # Player 1 choice
    player1_choice = input("1,2,3(or 'quit' to stop): ").lower()
    
    if player1_choice == "quit":
        print("Thanks for playing!")
        break  # Exit the game loop

    if player1_choice not in choices:
        print("Invalid choice. Please try again.")
        continue  # Go back to the start of the loop

    # Player 2 choice
    player2_choice = input("1,2,3(or 'quit' to stop): ").lower()

    if player2_choice == "quit":
        print("Thanks for playing!")
        break  # Exit the game loop

    if player2_choice not in choices:
        print("Invalid choice. Please try again.")
        continue  # Go back to the start of the loop

    # Determine and display the winner
    result = get_winner(player1_choice, player2_choice)
    print(result)