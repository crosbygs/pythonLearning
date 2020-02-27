def addToInventory(inventory,addedItems):
  for i in range(len(addedItems)):
    intOrigValue = inventory.setdefault(addedItems[i],0)
    inventory[addedItems[i]] = intOrigValue+1
  return inventory

def displayInventory(invList):
  runningTotal=0
  print('Inventory:')
  for k,v in invList.items():
    runningTotal+=v
    print(str(v)+' '+k)
  print('\nTotal number of items: '+str(runningTotal))

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)