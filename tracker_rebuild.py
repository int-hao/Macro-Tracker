from datetime import date
from statistics import mean

def get_number(prompt, low, high):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")
            continue
        if low <= value <= high:
            return value
        print(f"Please enter a number between {low} and {high}.")

calories = get_number("Calories: ", 0,2000)
protein = get_number("Protein: ", 0, 150)
carbs = get_number("Carbs: ", 0, 300)
fat = get_number("Fat: ", 0, 70)

macro_calories = protein*4 + carbs*4 + fat*9

if abs(calories - macro_calories) >100:
    print(f"Check: your macros add to {macro_calories} kcal, but you entered {calories} kcal.")
    print("One of the numbers might be off — check them before saving.")

class Day:
    def __init__(self, date, calories, protein, carbs, fat):
        self.date = date
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat
today = Day(date.today(), calories, protein, carbs, fat)

with open("macros_log.txt", "a") as f:
    f.write(f"{today.date}, {today.calories}, {today.protein}, {today.carbs}, {today.fat}\n")

class MacroLog:
    def __init__(self):
        self.days = []

    def add_day(self, day):
        self.days.append(day)

    def average_calories(self):
        return mean([day.calories for day in self.days])
    def average_protein(self):
        return mean([day.protein for day in self.days])
    def average_carbs(self):
        return mean([day.carbs for day in self.days])
    def average_fat(self):
        return mean([day.fat for day in self.days])


    def load(self, macros_log):
        with open(macros_log, "r") as f:
            for line in f:
                parts = line.strip().split(", ")
                day = Day(parts[0], int(parts[1]), int(parts[2]), int(parts[3]), int(parts[4]))
                self.add_day(day)

log = MacroLog()
log.load("macros_log.txt")
print(len(log.days))
print(log.average_calories())
print(log.average_protein())
print(log.average_carbs())
print(log.average_fat())
