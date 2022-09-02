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


        user_select = int(input()) 


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
    

    # have view last calc
    # edit this month
    # new calc
    # switch user
    # quit


    weeks = int(input('How many weeks are you scheduled for this month: '))

    for x in range(weeks):
        user.set_hours(x+1, float(input('Enter hours for week {}: '.format(x+1))))

    user.projection()

    user.save_user()





if __name__ == '__main__':
    main()