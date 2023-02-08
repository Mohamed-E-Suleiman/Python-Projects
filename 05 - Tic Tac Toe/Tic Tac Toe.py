print("-" * 100 , "\n")
print("\n"*10)
# --------------------------------------------------------------------

options = list('XOXOXOXOX')
d = {}
axes = []

for n in range(1,10):
    d[n] = ' '

def print_grid():
    global axes
    r1 = [d[1],d[2],d[3]]
    r2 = [d[4],d[5],d[6]]
    r3 = [d[7],d[8],d[9]]
    c1 = [d[1],d[4],d[7]]
    c2 = [d[2],d[5],d[8]]
    c3 = [d[3],d[6],d[9]]
    d1 = [d[1],d[5],d[9]]
    d2 = [d[3],d[5],d[7]]
    structure = [r1,r2,r3]
    axes = [r1,r2,r3,c1,c2,c3,d1,d2]
    for i in structure:
        print(*i, sep= " | ")

print('Welcome to TicTacToe!'+'\n'+'-'*50)

for option in options:
    while True:
        try:
            n = int(input(f"Player {option}'s Turn: "))
            break
        except:
            print('Please enter digits only!')
    while d[n] != ' ':
        n = int(input(f"Position already occupied!\nPlayer {option}'s Turn: "))
    d[n] = option
    print_grid()
    for axis in axes:
        if all(True if x == 'X' else False for x in axis):
            print('-'*50+'\n'+'Player X Wins! Congrats!'+'\n'+'-'*50)
            quit()
        if all(True if x == 'O' else False for x in axis):
            print('-'*50+'\n'+'Player O Wins! Congrats!'+'\n'+'-'*50)
            quit()

print('-'*50+'\n'+'It\'s a tie! Thanks for playing!'+'\n'+'-'*50)

# --------------------------------------------------------------------
print("\n"*10)
print("-" * 100 , "\n")