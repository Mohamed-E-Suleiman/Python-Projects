print("-" * 100 , "\n")
print("\n"*10)
# --------------------------------------------------------------------
from random import randint
l = []

def check(n):
    global tries
    if n < right_num:
        print('Your number is below target!')
        tries -= 1
    elif n > right_num:
        print('Your number is above target!')
        tries -= 1
    elif n == right_num:
        global won
        won = 1
        print('YOU WON, CONGRATS!!')

def start_game():
    print('Guess a number between 0 & 20!!')
    while True:
        if won == 1:
            break
        if tries > 1:
            n = int(input(f'You have {tries} tries left, Guess the correct number: '))
            l.append(str(n))
            check(n)
        elif tries == 1:
            ns = int(input(f'You have {tries} try left, Guess the correct number: '))
            l.append(str(ns))
            check(ns)
        elif tries == 0:
            print('Game Over!, Out of tries!')
            l.append('Game Over!')
            break

def keep_score():       
    f = open("Score History", "a")
    if l: f.write(' '.join(l) + '\n')
    f.close()

def show_history():
    f = open('Score History', 'r')
    s = f.read()
    if len(s) > 0: print(s)
    else: print('No Data!')
    f.close()

print('Hello there, Welcome to the game :)')
while True:
    print("-" * 100 , "\n")
    action = int(input('''Please Choose An Action:
1) Play
2) History
3) Quit
'''))
    print("-" * 100 , "\n")
    if action == 1:
        won = 0
        tries = 3
        right_num = randint(0,20)
        start_game()
    elif action == 2:
        try: show_history()
        except: print('No Entries Yet!')
    elif action == 3:
        print('Thanks for playing, Hope to see you soon :)')
        break
    else:
        print('Please Enter a Valid Action Number!: ')
        continue
    keep_score()


# --------------------------------------------------------------------
print("\n"*10)
print("-" * 100 , "\n")