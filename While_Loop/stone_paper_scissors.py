#WAP for game stone paper sicisor
import random
def game():
    if (comp=="p" and b=="s") or (b=='p' and comp=='c') or (b=='s' and comp=='p'):
        print("You Lose")
        print("You Had:",b,"Comp Had ",comp)
    elif (comp==b):
        print("It's a tie")
    else:
        print("You Win")
        print("You had:",b,"Comp had",comp)

while True:
    randomplay=random.randint(0,2)
    print("Comp turn (Stone(s),Paper(p),Sicissor(c).)")
    b = input("Players turn :Enter:(Stone(s),Paper(p),Sicissor(c)):")
    if randomplay == 0:
        comp = 's'
    elif randomplay == 1:
        com = 'p'
    elif randomplay == 2:
        comp = 'c'
    game()
    opt=input("Want a Rematch (y/n)??:\n")
    if opt != 'y':
        print("Ok!! Have Fun")
        break
