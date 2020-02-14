initList=['Dog', 'Cat', 'Racoon', 'Tiger', 'Elephant', 'Bear']

if len(initList) == 0:
  print('No list to operate on...')
else:
  for intIndex, strItem in enumerate(initList):
    if intIndex!=len(initList)-1:
      print(strItem,end=', ')
    else:
      print('and '+ strItem)