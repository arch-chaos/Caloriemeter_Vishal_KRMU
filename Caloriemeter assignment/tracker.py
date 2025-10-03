#Name - Vishal Jangir , Date - 03/10/2025 
#CALORIE TRACKER METER
from datetime import datetime
list_of_meals = []
calories_list = []
n = int(input("Enter the number of meals you want to enter :"))
for i in range(n):
    meal_name = input("Enter the name of the meal :")
    calorie_amount = float(input('Enter the amount of calorie intake:'))
    list_of_meals.append(meal_name)
    calories_list.append(calorie_amount)
sum_of_calories = sum(calories_list)
calorie_limit = float(input("Enter the calorie limit for the day :"))
#Limit Check
if sum_of_calories > calorie_limit:
    print("Warning!! you have taken {} more calories than the daily limit".format(sum_of_calories - calorie_limit))
else :
    print("Congratualtions!! you succusfully controlled the calorie intake of the day :)")
#Summary Table
print("  Meal Name \t Calories \n ---------------------------")
for i in range(n):
    print("  {} \t\t {}".format(list_of_meals[i],calories_list[i]))
print("  Total \t\t {}".format(sum_of_calories))
#Average Calculation
avg = sum_of_calories/n
print("Average: \t {}".format(avg))
#Bonus Task
choice = input("Do you want to save report , Enter 'Y/y' for yes and 'N/n' for no :")
if choice in 'Yy':
    with open('report.txt','w+') as f:
        f.write("{} List of meals = {} \ntotal clorie intake ={} \ndaily limit = {} \nAverage Consumption for the day = {}".format(datetime.now(),list_of_meals,sum_of_calories,calorie_limit,avg))
    print('Report saved succussfully')
    print("Thankyou!!")
else :
    print("Thankyou!!")