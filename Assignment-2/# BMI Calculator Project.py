# BMI Calculator Project
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight", "Try to gain weight with a nutritious diet."
    elif 18.5 <= bmi < 25:
        return "Normal", " Great! Maintain your current lifestyle."
    elif 25 <= bmi < 30:
        return "Overweight", " Consider exercising and watching your diet."
    else:
        return "Obese", " Consult a doctor for personalized advice."

try:
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))

    bmi = calculate_bmi(weight, height)
    category, tip = get_bmi_category(bmi)

    print(f" Your BMI is: {bmi:.2f}")
    print(f"Category: {category}")
    print(f" Health Tip: {tip}")

except ValueError:
    print(" Invalid input. Please enter numeric values only.")
