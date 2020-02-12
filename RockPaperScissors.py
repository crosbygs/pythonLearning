'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import random,sys
intNumWins=0
intNumLosses=0
intNumTies=0
strAnswer=''

print('ROCK, PAPER, SCISSORS')

while True:
    print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
    strAnswer=input()
    if strAnswer == 'q':
        sys.exit()

    intComputerTry=random.randint(1,3)

    if strAnswer=='r':
        print('ROCK versus...')
        if intComputerTry==1:
            print('ROCK')
            intNumTies=intNumTies+1
            print('It is a tie!')
        elif intComputerTry==2:
            print('PAPER')
            intNumLosses=intNumLosses+1
            print('So sorry... you lose')
        elif intComputerTry==3:
            print('SCISSORS')
            intNumWins=intNumWins+1
            print('You win!')
    elif strAnswer=='p':
        print('PAPER versus...')
        if intComputerTry==1:
            print('ROCK')
            intNumWins=intNumWins+1
            print('You win!')
        elif intComputerTry==2:
            print('PAPER')
            intNumTies=intNumTies+1
            print('It is a tie!')
        elif intComputerTry==3:
            print('SCISSORS')
            intNumLosses=intNumLosses+1
            print('So sorry... you lose')
    elif strAnswer=='s':
        print('SCISSORS versus...')
        if intComputerTry==1:
            print('ROCK')
            intNumLosses=intNumLosses+1
            print('So sorry... you lose')        
        elif intComputerTry==2:
            print('PAPER')
            intNumWins=intNumWins+1
            print('You win!')
        elif intComputerTry==3:
            print('SCISSORS')
            intNumTies=intNumTies+1
            print('It is a tie!')
    else:
        print('You entered an invalid input... Try again')
    print('%s Wins, %s Losses, %s Ties'%(intNumWins, intNumLosses, intNumTies))
        