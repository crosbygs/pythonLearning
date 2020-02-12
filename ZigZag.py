import time,sys

def printLine(numSpaces):
    outputStr="******"
    outputStr=outputStr.rjust(numSpaces+len(outputStr),' ')
    print(outputStr)
    time.sleep(0.1)
    
intSpaces = 5
intOperator = -1

try:
    while True:
        printLine(intSpaces)
        #print('DEBUG: intSpaces = '+str(intSpaces))
        
        intSpaces = intSpaces + intOperator
    
        if intSpaces == -1:
            intSpaces=1
            intOperator=1
        elif intSpaces == 6:
            intSpaces=4
            intOperator=-1
            
except KeyboardInterrupt:
    print()
    print('That was fun!!!')
    sys.exit()