from nis import match
from moneyUser import *
import json

def main():


    with open("data.json", "r") as file:
        data = json.load(file)

    
    user_list = {}
    #User menu
    print("Choose a user: ")
    print("0. Add new user")
    for index, name in enumerate(data["Users"].keys(), start=1):
        user_list[index] =  name
        print("{}. {}".format(index, name))

    #USER SELECT

    user_select = -1
    while user_select < 0:


        user_select = int(input('-')) 


        if user_select > 0 and user_select <= len(data["Users"]): #Choose pre existing user
            user = User() #Instansiate blank user object
            user.load_user(data["Users"][user_list[user_select]]) #overright user with saved data
        
        elif user_select == 0: #Make new user
            new_name = input("Enter your name: ")
            user = User(name = new_name)

        else:
            print("Selection invalid. Try again.")
            user_select = -1 

    # make a menu
    
    options = ['edit user', 'calculate this month', 'view user', 'switch user', 'delete user', 'quit']
    for index, option in enumerate(options, 1):
        print("{}. {}".format(index, option))

    selection = int(input('-'))


    #flow
    match selection:
        case 1:
            print('Edit...')

        case 2:
            print('calculate')

        case 3:
            print('view...')

        case 4:
            print('switch...')
        case 5:
            print('delete...')

        case 6:
            print('Goodbye...')

    # edit user - [pay, tax rate]
    # make new calculation this month
    # view last calc
    # switch user
    # quit


    # user.save_user()

    #put everything into a game loop
    





if __name__ == '__main__':
    main()