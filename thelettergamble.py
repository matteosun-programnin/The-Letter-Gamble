# Python Presents

#  The Letter Gamble
# Digital Slot Machine

import random

def spin_row():
    letters = ['A', 'B', 'C', 'D', 'E']
    
    return [random.choice(letters) for _ in range(3)]

def print_row(row):
    print("---------")
    print(" | ".join(row))
    print("---------")
    
def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == 'A':
            return bet * 3
        elif row[0] == 'B':
            return bet * 4
        elif row[0] == 'C':
            return bet * 5
        elif row[0] == 'D':
            return bet * 10
        elif row[0] == 'E':
            return bet * 20
    return 0
def main():
    balance = 100
    
    print("-The Letter Gamble-")
    print("-------------------")
    print("Letters: A B C D E ")
    print("-------------------")
    
    while balance > 0:
        print(f"Current Balance: ${balance}")
        
        
        bet = input("Place your bets here: ")
        
        
        if not bet.isdigit():
            print("wrong bet dude, i said the VALID bet")
            continue
            
        bet = int(bet)
        
        if bet > balance:
            print("Insufficient Funds")
            continue
            
        if bet <= 0:
            print("bet must be GREATER than 0")
            continue
        
        balance -= bet
        
        row = spin_row()
        print("Spinning...\n")
        print_row(row)
        
        payout = get_payout(row, bet)
    
        if payout > 0:
            print(f"You won ${payout}, so GG moment")
        else:
            print("Sorry, you've lost this round")
            
        balance += payout
        
        play_again = input("Do you want to spin again? (Y/N): ").upper()
        
        if play_again != 'N':
            continue
            
        if play_again != 'Y':
            break
     
              
    print(f"Game's over, Your final balance is ${balance} and try it again")
    
    
if __name__ == '__main__':
    main()




# NOTE - please do not mess or clean this code up because if you do that, this will not work