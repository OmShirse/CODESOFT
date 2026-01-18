import random
import time

player_score = 0
computer_score = 0
ties = 0

def show_title():
    print("\n" + "="*50)
    print("     🪨  ROCK - PAPER - SCISSORS  ✂️")
    print("="*50)

def get_player_choice():
    print("\nYour turn!")
    print("1 - Rock 🪨")
    print("2 - Paper 📄")
    print("3 - Scissors ✂️")
    
    while True:
        choice = input("\nWhat do you choose? (1/2/3 or rock/paper/scissors): ").lower()
        
        if choice == "1" or choice == "rock":
            return "rock"
        elif choice == "2" or choice == "paper":
            return "paper"
        elif choice == "3" or choice == "scissors":
            return "scissors"
        else:
            print("Invalid choice! Try again.")

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(player, computer):
    if player == computer:
        return "tie"
  
    if player == "rock" and computer == "scissors":
        return "player"
    elif player == "paper" and computer == "rock":
        return "player"
    elif player == "scissors" and computer == "paper":
        return "player"
    else:
        return "computer"

def show_choices(player, computer):
    print("\n" + "-"*50)
    print(f"You chose: {player.upper()}")
    
    print("Computer is choosing", end="")
    for i in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print()
    
    print(f"Computer chose: {computer.upper()}")
    print("-"*50)

def show_result(winner):
    if winner == "tie":
        print("\n🤝 It's a TIE!")
    elif winner == "player":
        print("\n🎉 YOU WIN! Nice job!")
    else:
        print("\n😔 You LOST! Better luck next time.")

def show_scores():
    print("\n" + "="*50)
    print("           SCOREBOARD")
    print("="*50)
    print(f"You: {player_score} wins")
    print(f"Computer: {computer_score} wins")
    print(f"Ties: {ties}")
    print("="*50)

def play_game():
    global player_score, computer_score, ties
    
    show_title()
    print("\nWelcome! Let's play Rock Paper Scissors!")
    print("Best of luck 🍀")
    
    
    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        
        show_choices(player_choice, computer_choice)
        
        winner = determine_winner(player_choice, computer_choice)
        
        if winner == "player":
            player_score += 1
        elif winner == "computer":
            computer_score += 1
        else:
            ties += 1
        
        show_result(winner)
        
        show_scores()
        
        play_again = input("\nPlay another round? (yes/no): ").lower()
        if play_again != "yes" and play_again != "y":
            break
    
    print("\n" + "="*50)
    print("         GAME OVER - FINAL SCORES")
    print("="*50)
    print(f"You: {player_score}")
    print(f"Computer: {computer_score}")
    print(f"Ties: {ties}")
    
    if player_score > computer_score:
        print("\n🏆 YOU'RE THE CHAMPION! Congrats!")
    elif computer_score > player_score:
        print("\n💻 Computer wins overall. Better luck next time!")
    else:
        print("\n🤝 It's a tie overall! You're evenly matched!")
    
    print("\nThanks for playing! See you next time 👋")

if __name__ == "__main__":
    play_game()
