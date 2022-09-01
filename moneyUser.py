from fileinput import close
import json

class User:
    
    
    def __init__(self, name = 'Guest', hourly_pay = 15.0, post_tax_percent = .846) -> None:
        self.name = name
        self.rate = hourly_pay
        self.take_home = post_tax_percent
        self.hours = {}
        self.last_calculated_total = 0
        return
    
    def set_hours(self, week, hours_working):
        self.hours[week] = hours_working
        return
        
    def set_pay(self, pay):
        self.rate = pay
        return
    
    def save(self):
        with open("data.json", "r+") as outfile:
            data = json.load(outfile)
            data["Users"][self.name] = self.__dict__
            outfile.seek(0)
            json.dump(data, outfile, indent=4)
        return
            
    def projection(self):
        hours = sum(self.hours.values())
        total_income = hours * self.rate * self.take_home
        self.last_calculated_total = total_income
        print('Your projected income is ${:.2f} this month'.format(total_income))
        return