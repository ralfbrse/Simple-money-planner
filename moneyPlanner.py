from moneyUser import *
import json


print("Choose a user: ")

with open("data.json", "r") as dataSer:
    data = json.load(dataSer)

user_list = enumerate(data["Users"].keys(), start=1)

print("0. Add new user")
for index, name in user_list:
    print("{}. {}".format(index, name))

# FIXME make user selections work
# and load data from json into py object to work with

pause = input()
user1 = User(name="Dave")


# make a menu
# have view last calc
# edit this month
# new calc
# switch user
# quit


weeks = int(input('How many weeks are you scheduled for this month: '))

for x in range(weeks):
    user1.set_hours(x+1, float(input('Enter hours for week {}: '.format(x+1))))

user1.projection()

user1.save()
