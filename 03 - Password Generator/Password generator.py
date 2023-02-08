'''
1) ask the user for a password length that is 6 characters or more
2) get the character sources and randomize them
3) decide what percantage of the rquired password you're gonna take from each source
4) put all the randomly picked elements together and maybe shuffle them one more time
5) print the output

'''
import string as s, random as r

pass_length = input('Please enter how many characters you want your password to be (Min. 6): ')
password = []
while True:
    try:
        pass_length = int(pass_length)
        if pass_length < 6:
            print('You need at least 6 characters!')
            pass_length = input('Please try again: ')
        else: break
    except:
        pass_length = input('Please enter numbers only): ')
    
l1 = list(s.ascii_lowercase)
l2 = list(s.ascii_uppercase)
l3 = list(s.digits)
l4 = list(s.punctuation)

r.shuffle(l1)
r.shuffle(l2)
r.shuffle(l3)
r.shuffle(l4)

twenty = round(pass_length * (20/100))
thirty = round(pass_length * (30/100))

for _ in range(twenty):
    password.append(l3[r.randint(0, len(l3)-1)])
    password.append(l4[r.randint(0, len(l4)-1)])

for _ in range(thirty):
    password.append(l1[r.randint(0, len(l1)-1)])
    password.append(l2[r.randint(0, len(l2)-1)])

r.shuffle(password)
print(''.join(password))