'''
AUTHOR: CHISOM NWACHUKWU

PURPOSE: Learning Activity (1 of 2): Lists
'''

features = ['Add item', 'View cart', 'Remove item', 'Compute total', 'Quit']
action = ''
shopping_cart = []
price_list = []
sums = 0

print('\nWelcome to the Shopping Cart Program!')
print('\nPlease select one of the following:')

for i in range(len(features)):
    print(f'{i + 1}. {features[i]}')

while action != 5:
    print()

    action = int(input('Please enter an action: '))

    item = ''
    price = ''

    if action == 1 :
        print('Type in the items you\'d like to add? (type "stop" when finished)')
        while item != 'stop':
            item = input('What item would you like to add? ')

            if item != 'stop':
                price = float(input(f'How much is {item}? '))
                shopping_cart.append(item.title())
                price_list.append(price)
                print(f'{item} has been added to cart')
                print()

    elif action == 2:
        print('\nThe contents of the shopping cart are: ')
        if len(shopping_cart) == 0:
            print('Your cart is empty!')
        else:
            for i in range(len(shopping_cart)):
                for j in range(len(price_list)):
                    if i == j:
                        print(f'{i + 1}. {shopping_cart[i]} - {price_list[j]}')
                    
    elif action == 3:
        print()
        if len(shopping_cart) == 0:
            print('Your cart is empty!')
        else:
            for i in range(len(shopping_cart)):
                for j in range(len(price_list)):
                    if i == j:
                        print(f'{i + 1}. {shopping_cart[i]} - {price_list[i]:.2f}')

        print('\nWhich item would you like to remove? ')
        remove_item = int(input('Item number: '))

        if remove_item > len(shopping_cart) or remove_item <= 0:
            print('Sorry, that is not a valid item number')
        else:
            indexed = remove_item - 1
            shopping_cart.pop(indexed)
            price_list.pop(indexed)
        print('Item removed!')

    elif action == 4:
        for total in price_list:
            sums += total
        # sums = sum(price_list)
        print(f'\nThe total price of the items in the shopping cart is {sums:.2f}')

    elif action == 5:
        print('Thank you. Goodbye.')

    else:
        print("Invalid action. Please choose a number between 1 and 5.")