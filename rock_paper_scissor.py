import random
def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r','p','s'])

    is_win(user,computer)

def is_win(user,computer):
    #r > s, s > p, p > r
    if (user=='r' and computer=='s') or (user=='s'and computer=='p') or(user=='p'and computer=='r'):
        print("You Win !!!")
    elif user == computer:
        print("Match Is Tie !!!")
    else:
        print("Computer Win !!!")

play()    
