print("welkom bij de sinterklaas verlanglijst! Hier kunt u cadeau's invullen dat uw op uw verlanlijst wilt. Als u klaar bent typed u KLAAR!")

my_list = []
while True:
    cadeaus = input('voer cadeau in: ')
    
    if cadeaus == 'KLAAR!':
        print('gebruiker typte KLAAR!')
        break

    my_list.append(cadeaus)
my_list.sort()
print(my_list)

