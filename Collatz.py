def funcCollatz(intInput):
    if intInput%2==0:
        intResult=intInput//2
    else:
        intResult=3*intInput+1
    return int(intResult)

try:    
    intOperNum = int(input('What is your starting number? '))

    intCycleCount = 0
    while intOperNum!=1:
        intOperNum=funcCollatz(intOperNum)
        intCycleCount=intCycleCount+1
        print('Cycle: '+str(intCycleCount)+'   '+str(intOperNum))

    print('All done!  See, it worked.')    
    
except ValueError:
    print('You have to enter an integer')