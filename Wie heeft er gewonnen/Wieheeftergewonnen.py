my_list = []
print("Hier gat u zo uw spelers invoeren.")
while True:
    user_input = input('voer speler in: ')

    
    if user_input == '':
        print('User pressed Enter')
        break

    my_list.append(user_input)
print(my_list)
