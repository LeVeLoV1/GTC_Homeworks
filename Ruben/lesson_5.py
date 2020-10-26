


# ex_2 shoping
cost_list = []
check_count = 0


def add_item(itemName, itemCost):
    global name
    name = itemName
    global cost
    cost = itemCost
    cost_list.append(itemCost)
    global result
    result = sum(cost_list)
    global item_count
    item_count = len(cost_list)



def print_receipt():

    global check_count
    if cost_list:
        check_count += 1
        print('Чек', check_count, 'Всего предметов:', item_count)
        for _ in range(item_count):
            print(name, '-', cost)
        print('Итого:', result)
        print('_____')
    else:
        print('корзина пустая')


add_item('abo', 3)
print_receipt()


