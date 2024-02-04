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
    print("Eee! You are over weight.") 
else:  
    print("Seesh! You are obese.") 
