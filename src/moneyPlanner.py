from src import menus


def main():
    #USER SELECT

    user = menus.Menu.user_select()
    
    # make a menu
    while True:
        if user == None:
            print("Goodbye...")
            return
        print()
        print("Current user: {}".format(user.get_name()))
        selection = menus.Menu.main_menu()
    #flow
        
        match selection:
            case 1:
                user.set_hours()
                print()
                while True:
                    save_user = input("Would you like to save your changes? [y/n]: ")
                    if save_user == 'y':
                        user.save_user()
                        break
                    elif save_user =='n':
                        print("Discarding...")
                        break
                    else:
                        print('Enter valid input.')
                
            case 2:
                user.set_pay()
                print()

            case 3:
                print(user.projection())
                print()

            case 4:
                print(user.get_pay())
                print(user.get_hours())
                print(user.projection())
                print()

            case 5:
                user = menus.Menu.user_select()
            case 6:
                sel = input("Permenantly delete user? [y/n]: ")
                if sel == 'y':
                    user.delete_user()
                    user = menus.Menu.user_select()
                elif sel == 'n':
                    print("Operation cancelled...")
                else:
                    print("Select valid option")

            case 7:
                print('Goodbye...')
                break