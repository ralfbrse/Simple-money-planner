import json
from . import User


class Menu:

    def user_select():

        with open("src/data.json", "r") as file:
            data = json.load(file)

    
        user_list = {}
        #List out users
        print("Choose a user: ")
        print("0. Add new user")
        for index, name in enumerate(data["Users"].keys(), start=1):
            user_list[index] =  name
            print("{}. {}".format(index, name))

        print("Leave blank and press enter to quit.")
        #Select your option
        sel = -1
        while sel < 0:

            

            try:
                sel = int(input('$ ')) 
            
            except:
                return None
            #Select existing user
            if sel > 0 and sel <= len(data["Users"]): #Choose pre existing user
                user = User.User() #Instansiate blank user object
                user.load_user(data["Users"][user_list[sel]]) #overright user with saved data
            
            #Make new user
            elif sel == 0: #Make new user
                new_name = input("Enter your name: ")
                user = User.User(name = new_name)
                user.set_pay()
                user.save_user()
                
            #Invalid selection
            else:
                print("Selection invalid. Try again.")
                sel = -1 

        return user

    def main_menu():
        print()
        options = ['edit hours', 'edit pay', 'calculate this month', 'view user', 'switch user', 'delete user', 'quit']
        for index, option in enumerate(options, 1):
            print("{}. {}".format(index, option))
        sel = int(input('$ '))
        print()
        print()
        return sel