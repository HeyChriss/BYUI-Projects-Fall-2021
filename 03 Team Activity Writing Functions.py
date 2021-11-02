from datetime import datetime


def main():
    # Get the user's gender, birthdate, height, and weight.
    birth = input (' Enter your Date of birth (yyyy-mm-dd): ')
    inch = float (input (' Enter your height in US inches: '))
    lb = float (input (' Enter your weight in US pounds: '))
    gender = input ('Enter your gender (M or F): ').upper


    # Call the compute_age, kg_from_lb, cm_from_in, body_mass_index,
    age = compute_age(birth)
    weight = kg_from_lb(lb)
    height = cm_from_in(inch)
    bmi = body_mass_index(weight, height)
    bmr = basal_metabolic_rate(gender, weight, height, age)

    # Print the results for the user to see.
    print (f'Age (years): {age}')
    print (f'Weight (kg): {weight:.2f}')
    print (f'Height (cm): {height:.1f}')
    print (f'Body mass index: {bmi:.1f}')
    print (f'Basal metabolic rate (kcal/day): {bmr:.0f}')
    


def compute_age(birth):
    """Compute and return a person's age in years.
    Parameter birth: a person's birthdate stored as
        a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    birthday = datetime.strptime(birth, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the birthday in years.
    age = today.year - birthday.year

    # If necessary, subtract one from the difference.
    if birthday.month > today.month or \
        (birthday.month == today.month and birthday.day > today.day):
        age -= 1

    return age


def kg_from_lb(lb):
    """Convert a mass in pounds to kilograms.
    Parameter lb: a mass in US pounds.
    Return: the mass in kilograms.
    """
    Weight = lb * 0.45359237 
    return Weight


def cm_from_in(inch):
    """Convert a length in inches to centimeters.
    Parameter inch: a length in inches.
    Return: the length in centimeters.
    """
    height = inch * 2.54
    return  height


def body_mass_index(weight, height):
    """Calculate and return a person's body mass index (bmi).
    Parameters:
        weight must be in kilograms.
        height must be in centimeters.
    Return: a person's body mass index.
    """
    bmi = weight / (height**2) * 10000
    return bmi 


def basal_metabolic_rate(gender, weight, height, age):
    """Calculate and return a person's basal metabolic rate (bmr).
    Parameters:
        weight must be in kilograms.
        height must be in centimeters.
        age must be in years.
    Return: a person's basal metabolic rate in kcal per day.
    """
    if gender == 'M': 
        bmr = 88.362 + 13.397 * weight + 4.799*height - 5.677 * age 
    else:
         bmr = 447.593 + 9.247 *weight + 3.098 *height - 4.330 * age
    return bmr


# Call the main function so that
# this program will start executing.
main()

