
from ctypes import sizeof
from moneyUser import *
import json
from types import SimpleNamespace


print("Choose a user: ")

with open("data.json", "r") as dataSer:
    data = json.load(dataSer)

user_enum = enumerate(data["Users"].keys(), start=1)
user_list = {}
print("0. Add new user")
for index, name in user_enum:
    user_list[index] =  name
    print("{}. {}".format(index, name))

# FIXME make user selections work
user_select = -1

while user_select == -1:
    
    user_select =int(input())
    if user_select > 0 and user_select <= len(data["Users"]):
        user = User()
        user.load_user(data["Users"][user_list[user_select]])
    # and load data from json into py object to work with
    elif user_select == 0:
        new_name = input("Enter your name: ")
        user = User(name = new_name)
    else:
        print("Select a valid option")
        user_select = -1 

print(user.name)

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

user.save()
