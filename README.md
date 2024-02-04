# BMI Calculator

This Python script calculates Body Mass Index (BMI) based on user input for height and weight.

## Table of Contents

- [Introduction](#introduction)
- [How to Use](#how-to-use)
- [Example](#example)
- [BMI Categories](#bmi-categories)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The BMI Calculator is a simple Python script that takes user input for height and weight and calculates the BMI. It then categorizes the BMI into different health categories.

## How to Use

1. Run the script `bmi_calculator.py`.
2. Enter your height in centimeters when prompted.
3. Enter your weight in kilograms when prompted.
4. The script will calculate and display your Body Mass Index along with the corresponding health category.

## Example

```python
# input values from the users  
height = float(input("Enter the height in cm: "))  
weight = float(input("Enter the weight in kg: ")) 

# function defining for BMI  
BMI = weight / (height/100)**2  

# printing the BMI  
print("Your Body Mass Index is", BMI)  

# if-elif-else conditions for result
if BMI <= 18.5:  
    print("Oops! You are underweight.")  
elif BMI <= 24.9:  
    print("Awesome! You are healthy.")  
elif BMI <= 29.9:  
    print("Eee! You are overweight.") 
else:  
    print("Seesh! You are obese.") 
```

## BMI Categories

- **Underweight**: BMI <= 18.5
- **Healthy Weight**: 18.5 < BMI <= 24.9
- **Overweight**: 24.9 < BMI <= 29.9
- **Obese**: BMI > 29.9

## Contributing

If you'd like to contribute to the project, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
