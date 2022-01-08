# In this I will make an BMI(Body mass Index calculator) but updated version of the last one
# It is given as: body mass/height*height

# Taking input of body weight in kg and height in meter
weight = int(input("Enter you body weight Sir/Ma'am in kilogram(kg): "))
height = float(input("Enter you height Sir/Ma'am in meter(m): "))

# Calculate BMI
bmiValue = float("{0: .2f}".format(weight / height ** 2))

#Giving output as BMI and also the condition relate to it
if bmiValue <= 18.5:
    print(f"Your BMI value is {bmiValue} and you are underweight")
elif 18.5 < bmiValue <= 25:
    print(f"Your BMI value is {bmiValue} and you are normal weight")
elif 25 < bmiValue <= 30:
    print(f"Your BMI value is {bmiValue} and you are over weight")
elif 30 < bmiValue <= 35:
    print(f"Your BMI value is {bmiValue} and you are obese")
else:
    print(f"Your BMI value is {bmiValue} and you are clinically obese")