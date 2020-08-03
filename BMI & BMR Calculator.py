print("Assalamu Alaikum Wa Rahmatullah. Welcome to BMI & BMR Calculator.")


cal=input("What would you like  to calculate?\n1) BMI\n2) BMR\nYour Answer:")

if cal == "BMI" or cal == "1" or cal == "bmi":
    height = float(input("Enter your height in Metre:"))
    weight = float(input("Enter your weight in KG:"))
    bmi = weight/height**2
    print("Your BMI: "+str(bmi))
    if bmi <= 18.4:
        print("Your body weight is too low.You need to take proper food habits.")
    elif bmi >= 18.5 or bmi <= 24.9:
        print("You have standard weight.")
    elif bmi >= 25 or bmi <= 29.9:
        print("Your body weight is excess. You need exercise to reduce overweight.")
    elif bmi >= 30 or bmi <= 34.9:
        print("The first stage of obesity. Selective food and exercise are required for you.")
    elif bmi >= 35 or bmi <= 39.9:
        print("The second stage of obesity. Moderate diet and exercise are required for you.")
    else:
        print("You have extra obesity and risk of death! You need to doctor's advice.")


else:
    gender = input("What's your gender? : ")
    height = float(input("Enter your height in Centi-Metre: "))
    weight = float(input("Enter your weight in KG: "))
    age = float(input("Enter your age in year: "))
    if gender == "Male" or "male" or "m":
        bmr = 66+(13.7*weight)+(5*height)-(6.8*age)
        print("Your BMR: "+str(bmr))
    else:
        bmr = 655+(9.6*weight)+(1.8*height)-(4.7*age)
        print("Your BMR: " + str(bmr))
