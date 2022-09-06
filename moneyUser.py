import json


class User:
    
    
    def __init__(self, name = "Default", hourly_pay = 0, post_tax_percent = .846) -> None:
        
        self.name = name
        self.rate = hourly_pay
        self.take_home = post_tax_percent
        self.hours = {}
        self.last_calculated_total = 0.0
        return
    
    def get_name(self):
        return self.name

    def set_hours(self):
        weeks = int(input('How many weeks are you scheduled for this month: '))        
        if weeks > 5:
            print("That cant be right...")
            return
        self.hours = {}
        

        for x in range(weeks):
            self.hours[x+1] = float(input('Enter hours for week {}: '.format(x+1)))
        self.projection()
        return
        
    def set_pay(self):
        pay = int(input('Input new pay rate: '))
        self.rate = pay
        self.projection()
        return

    def get_hours(self):
        return "Hours {}".format(self.hours)

    def get_pay(self):
        return "Hourly pay: ${}".format(self.rate)

    def get_last_calculated_total(self):
        return self.last_calculated_total

    def projection(self):
        hours = sum(self.hours.values())
        total_income = hours * self.rate * self.take_home
        self.last_calculated_total = total_income
        return 'Your projected income is ${:.2f} this month'.format(self.get_last_calculated_total())
    
    def save_user(self):
        with open("data.json", "r") as r:
            data = json.load(r)
        data["Users"][self.name] = self.__dict__
        with open("data.json", "w") as w:
            json.dump(data, w, indent=4)
        return

    def delete_user(self):
        with open("data.json", "r") as r:
            data = json.load(r)
        data["Users"].pop(self.name)
        with open("data.json", "w") as w:
            json.dump(data, w, indent=4)
        return
        

    def load_user(self, dict1):
        self.__dict__.update(dict1)
        return
            
    