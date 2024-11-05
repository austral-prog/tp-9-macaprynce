
def create_inventory(items):
    mydict = dict()
    for i in items:
        if i in mydict:
            mydict[i] +=1
        else:    
            mydict[i] = 1

    return mydict

def add_items(inventory, items):
    for i in items:
        if i not in inventory:
            inventory[i] = 1
        else:
            inventory[i] += 1

    return inventory

def decrement_items(inventory, items):
    for i in items:
        if inventory[i]==0:
            inventory [i] = 0
        else: 
            inventory [i] -= 1
    
    return inventory

def remove_item(inventory, item):
    for i in inventory.keys():
        if i == item:
            del inventory[i]
            break
    return inventory

def list_inventory(inventory):
    my_list=[]
    for i,x in inventory.items():
      if x > 0:
        my_tuple = (i,x)
        my_list.append(my_tuple)
    return my_list

