#Sree Parvati
#5/11/2025
#Daily Calorie Tracker CLI

#printed Welcome Message
print ( "Welcome to Calorie Tracker ! It helps you to keep a track of your calorie intake helping  you to maintain your health.")


#input number of meals
num_of_meals = int(input("How many meals you want to enter?",))
#blank list
meal_name = []
calorie = []


#loop for meal name and calorie input
for i in range (num_of_meals):
    name = input(f"Type your meal name.{i+1}:")
    c_alorie = float(input(f"Enter your meal calorie.{name}:"))
    meal_name.append(name)            #making list
    calorie.append(c_alorie) 



#printing list
print("meal name:",meal_name)
print("calorie:",calorie)

#printing total calorie
sum_ = sum(calorie)
print(sum_)
#printing average calorie
average_ = sum_/ num_of_meals
print(average_)

#input daily calorie limit intake
limit_of_daily_calorie_intake = float(input("What is you aim of daily calorie limit?",))
#Using if-else statements to compare daily calorie limit and total calorie intake
if limit_of_daily_calorie_intake < sum_:
    print("You have crossed beyond your daily calorie limit.")
else: 
    print("You have maintained your daily calorie limit.")

#table
print("\nMeal Name  \tCalories")
print("-------------------------------------------------------------")
for x in range(num_of_meals):

    print(f"{meal_name[x]:<15} \t{calorie[x]:>5}")
print(f"{'Total Calorie :':<15} \t{sum_:>5}")
print(f"{'Average :':<15} \t{average_:>5}")

from datetime import datetime
# bonus task
save_file = input("Do you want to save your report?(yes/no): ")

if save_file.lower() == "yes":
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("calorie_report.txt", "w") as f:
        f.write("=== Calorie Report ===\n\n")
        f.write(f"Date & Time:{timestamp}\n\n")
        f.write("Meals:\n")
        for i in range(num_of_meals):
            f.write(f"{meal_name[i]:<15}{calorie[i]:>8}\n")

        total_calories = sum(calorie)
        f.write(f"{'Total Calories:':<15}{total_calories:>5}\n")
        f.write(f"{'Average:':<15}{average_:>5}\n")
        f.write(f"{'Daily Limit:':<15}{limit_of_daily_calorie_intake:>5}\n")

        if total_calories > limit_of_daily_calorie_intake:
            f.write("\nStatus: You have crossed your daily calorie limit.\n")
        else:
            f.write("\nStatus: You have maintained your daily calorie limit.\n")

    print("Session saved successfully to calorie_report.txt")



