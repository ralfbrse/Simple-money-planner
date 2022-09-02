import json


class User:
    
    
    def __init__(self, name = "Default", hourly_pay = 0, post_tax_percent = .846) -> None:
        
        self.name = name
        self.rate = hourly_pay
        self.take_home = post_tax_percent
        self.hours = {}
        self.last_calculated_total = 0
        return
    
    
    def set_hours(self):
        weeks = int(input('How many weeks are you scheduled for this month: '))

        for x in range(weeks):
            self.hours[x+1] = float(input('Enter hours for week {}: '.format(x+1)))
        self.projection()
        return
        
    def set_pay(self):
        pay = int(input('Input new pay rate: '))
        self.rate = pay
        return
    
    def save_user(self):
        with open("data.json", "r+") as outfile:
            data = json.load(outfile)
            data["Users"][self.name] = self.__dict__
            outfile.seek(0)
            json.dump(data, outfile, indent=4)
        return

    # def delete_user(self):
    #     #FIXME
    #     return

    def load_user(self, dict1):
        self.__dict__.update(dict1)
        return
            
    def projection(self):
        hours = sum(self.hours.values())
        total_income = hours * self.rate * self.take_home
        self.last_calculated_total = total_income
        print('Your projected income is ${:.2f} this month'.format(total_income))
        return