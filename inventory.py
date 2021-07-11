from copy import copy

# stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    total = 0
    print('Inventory:')
    for k,v in inventory.items():
        total += v
        print(f'{v} {k}')
    print('Total number of items: ' + str(total))

def addToInventory(inventory, items):
    result = copy(inventory)
    for item in items:
        result.setdefault(item, 0)
        result[item] += 1
    return result

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

