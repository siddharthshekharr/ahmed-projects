"""
Blackjack Game

This program implements the classic casino card game Blackjack with the following features:

Game Specifications:
1. Card System:
    - Cards are represented by their numerical values (2-10, face cards = 10, Ace = 11/1)
    - Aces automatically adjust from 11 to 1 if the hand would bust
    - A Blackjack (21 with exactly 2 cards) is handled as a special case
    
2. Gameplay Features:
    - Player starts with two cards and can choose to:
    * Hit ('y'): Take another card
    * Stand ('n'): Keep current hand
    * View Stats: View game history and performance
    
    - Computer dealer follows house rules:
    * Must hit on 16 or below
    * Must stand on 17 or above
    
    - Game ends when:
    * Player stands
    * Player or dealer gets Blackjack
    * Player or dealer busts (goes over 21)
    
3. Statistics System:
    - Each game result is saved to 'blackjack_stats.txt' with:
    * Timestamp of the game
    * Game outcome (Win/Lose/Draw)
    * Final scores of both player and computer
    
    - Statistics tracking includes:
    * Complete game history
    * Total wins, losses, and draws
    * Win rate percentage
    * Viewable during gameplay or at exit
"""

import random
import datetime

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

print(logo)

def deal_card():
    """Returns a random card from the deck"""
    # List includes Ace(11) and face acrds(10)
    # cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # card = random.choice(cards)
    # return card
    cards = [n for n in range(2, 11)]
    cards.extend([10, 10, 10, 11])
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    # Check for blackjack
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # Convert Ace to 1 if bust
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    """Compares the user score u_score against the computer score c_score."""
    # Check all winning/losing conditions
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"
    
def save_game_stats(result, user_score, computer_score):
    """Saves the game result and scores to a file with timestamp"""
    # Add timestamp to result
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("blackjack_stats.txt", "a") as file:
        file.write(f"{timestamp} | {result} | Player: {user_score} | Computer: {computer_score}\n")
        
def display_game_stats():
    """Shows game history and calculates stats"""
    try:
        with open("blackjack_stats.txt", "r") as file:
            print("\n=== Game History ===")
            print("Time                 | Result                          | Scores")
            print("-" * 70)
            
            # Track game outcomes
            wins = 0
            losses = 0
            draws = 0
            
            # Count each type of result
            for line in file:
                print(line.strip())
                line_lower = line.lower()
                if "win" in line_lower:
                    wins += 1
                elif "lose" in line_lower:
                    losses += 1
                elif "draw" in line_lower:
                    draws += 1
            
            # Display overall statistics
            print("\n=== Overall Statistics ===")
            print(f"Wins: {wins}")
            print(f"Losses: {losses}")
            print(f"Draws: {draws}")
            total_games = wins + losses + draws
            if total_games > 0:
                win_rate = (wins / total_games) * 100
                print(f"Win Rate: {win_rate:.1f}%")
            
    except FileNotFoundError:
        print("\nNo game history found. Play some games first!")

def play_game():
    print(logo)
    # Setup initial hands
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    # Deal starting cards
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Player's turn loop
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # Check for game ending conditions
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # Get player's choice
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer's turn - hit until 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Show final hands and save result
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    result = compare(user_score, computer_score)
    print(result)
    
    # Save game statistics
    save_game_stats(result, user_score, computer_score)

# Game start/restart loop
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()

# Show stats at end
print("\nFinal Statistics:")
display_game_stats()