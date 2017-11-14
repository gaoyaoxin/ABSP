def displayInventory(inventory):
	print("Inventory:")
	item_total = 0
	for k, v in inventory.items():
		print(str(v) + ' ' + k)
		item_total += v
	print("Total number of items: " + str(item_total))


def addToInventory(inventory, addedItems):
	newDict = {}
	for i in range(len(addedItems))

		count.setdefault(i, 0)
		count[i] += 1




	if addedItems[i] in inventory.keys():


		
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)