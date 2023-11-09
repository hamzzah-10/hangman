import random 

def play():
    user = input("For rock 'r', For paper 'p', For siccors 's': ").lower()
    computer = random.choice(['r', 'p', 's'])
    print(f"Computer Choice {computer}" )
    if user == computer:
        return "tie"

    if is_win(user, computer):
        return 'You Won!!!'
    
    return 'You Lost :('
# r > s, s > p, p > r

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'r') or (player == 'p' and opponent == 'r'): 
        return True

print(play())    