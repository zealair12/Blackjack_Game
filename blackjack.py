from blackjack_helper import *

# User's Turn
user_hand = draw_starting_hand("YOUR")
done = ""
while user_hand < 21 and done != 'n':
    done = input(f"You have {user_hand}. Hit (y/n)? ")
    if done == 'y':
        user_hand += draw_card()
    elif done != 'n':
        print("Sorry I didn't get that.")
        
print_end_turn_status(user_hand)

# Dealer's Turn
dealer_hand = draw_starting_hand("DEALER")
while dealer_hand < 17:
    dealer_hand += draw_card()
    
print_end_turn_status(dealer_hand)

# Determine Game Result
print_end_game_status(user_hand, dealer_hand)
