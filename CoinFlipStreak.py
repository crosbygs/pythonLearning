import random

numberOfStreaks = 0

for experimentNumber in range(10000):
  flipResult=[]
  for intIndex in range(100):
      if random.randint(0, 1) == 0:
          flipResult.append('H')
      else:
          flipResult.append('T')

  intCurrentStreak = 0
  strPrevResult = ''

  for strResult in flipResult:
    if strResult == strPrevResult:
        intCurrentStreak += 1
    else:
        if intCurrentStreak >= 6:
            numberOfStreaks += 1
        intCurrentStreak = 0
    strPrevResult = strResult

#  if experimentNumber % 100 == 0:
#    print('Experiment: ' + str(experimentNumber) + ' Chance of streak = ' + str(numberOfStreaks /((experimentNumber + 1) * 100)) + ' Current Streak = ' + str(numberOfStreaks))

print('Chance of streak: %s%%' % (numberOfStreaks / (experimentNumber + 1)))
