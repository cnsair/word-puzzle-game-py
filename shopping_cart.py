'''
AUTHOR: CHISOM NWACHUKWU

PURPOSE: Learning Activity (1 of 2): Lists
'''

features = ['Add item', 'View cart', 'Remove item', 'Compute total', 'Quit']

action = ''

print('\nWelcome to the Shopping Cart Program!')
print('\nPlease select one of the following:')

for i in range(len(features)):
    print(f'{i + 1}. {features[i]}')

while action != 5:

    action = int(input('Please enter an action: '))

    shopping_cart = []
    price_list = []
    item = ''
    price = ''
    count = 0
    sums = 0

    if action == 1 :
        print('Type in the items you\'d like to add? (type "stop" when finished)')
        while item != 'stop':
            item = input('What item would you like to add? ')

            if item != 'stop':
                # while price != float():
                price = float(input(f'How much is {item}? '))
                shopping_cart.append(item.title())
                price_list.append(price)
                print(f'{item} has been added to cart')
                print()
                for i in range(len(shopping_cart)):
                    for j in range(len(price_list)):
                        if i == j:
                            print(f'{i + 1}. {shopping_cart[i]} - {price_list[j]}')

    elif action == 2:
        print('\nThe contents of the shopping cart are: ')
        for i in range(len(shopping_cart)):
            for j in range(len(price_list)):
                if i == j:
                    print(f'{i + 1}. {shopping_cart[i]} - {price_list[j]}')

    elif action == 3:
        print('\nWhich item would you like to remove? ')
        remove_item = int(input('Item number: '))

        if remove_item > len(shopping_cart):
            print('Sorry, that is not a valid item number')
        else:
            indexed = remove_item - 1
            shopping_cart.pop(indexed)
            price_list.pop(indexed)
        print('Item removed!')

    # print('\nThe contents of the shopping cart are: ')
    # for i in range(len(shopping_cart)):
    #     for j in range(len(price_list)):
    #         if i == j:
    #             print(f'{i + 1}. {shopping_cart[i]} - {price_list[j]}')

    elif action == 4:
        for total in price_list:
            sums += total
        
        print(f'\nThe total price of the items in the shopping cart is {sums}')

print('Thank you. Goodbye')