import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    print(f"First Roll: [{die1}] [{die2}] = {total}")
    return total

def play_round(wallet):
    print("\nReady to play!")
    print(f"You have ${wallet} in your wallet.")

    bet = get_player_bet(wallet)
    print(f"\nFirst Roll: ", end="")
    point = roll_dice()

    if point in (7, 11):
        print(f"\nWINNER!! You won ${bet}")
        return bet
    elif point in (2, 3, 12):
        print(f"\nSORRY!! You lost ${bet}")
        return -bet
    else:
        print(f"\nYour point is:--{point}--\nrolling again...\n")
        return roll_to_point(point, bet)

def roll_to_point(point, bet):
    while True:
        print(f"Rolled: ", end="")
        total = roll_dice()

        if total == 7:
            print(f"\nSORRY!! You lost ${bet}")
            return -bet
        elif total == point:
            print(f"\nWINNER!! You won ${bet}")
            return bet

def get_player_bet(wallet):
    while True:
        try:
            bet = int(input(f"What's your bet? "))
            if 0 < bet <= wallet:
                return bet
            else:
                print(f"\nSorry, you only have ${wallet}. What's your bet? ", end="")
        except ValueError:
            print("\nInvalid input. Please enter a valid number. What's your bet? ", end="")

def initialize_game():
    print("\n-- Welcome to PY-CRAPS --")
    player = input("\nWhat is your name? ")
    
    while True:
        try:
            wallet_str = input(f"Hi {player}. How many chips do you want to buy? ")
            if not wallet_str:
                raise ValueError("Please enter a value.")
            
            wallet = int(wallet_str)
            if wallet <= 0:
                raise ValueError("Please enter a positive value.")
            
            break  # Break out of the loop if input is valid
        except ValueError as e:
            print(f"Invalid input: {e}")

    return player, wallet

def finish_game(player_name, wallet):
    if wallet <= 0:
        print(f"\nYou are BROKE. Sorry {player_name}, come back and play again sometime.")
    else:
        print(f"\nGoodbye, {player_name}! You are leaving with ${wallet}.")

def ask_to_play_again():
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    return play_again == "yes"

def play_multiple_games():
    player, wallet = initialize_game()

    while wallet > 0:
        wallet_change = play_round(wallet)
        wallet += wallet_change

        if wallet <= 0:
            break

        play_again = ask_to_play_again()
        if not play_again:
            break

    finish_game(player, wallet)

# Run the entire program
play_multiple_games()
