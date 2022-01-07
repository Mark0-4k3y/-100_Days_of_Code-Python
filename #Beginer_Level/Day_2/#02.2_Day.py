# In this I will make an BMI(Body mass Index calculator)
# It is given as: body mass/height*height

# Taking input of body weight and height
weight = int(input("Enter you body weight Sir/Ma'am in kilogram(kg): "))
height = float(input("Enter you height Sir/Ma'am in meter(m): "))

# Giving output as BMI
print("Your BMI is: ", str(int(weight/height ** 2))+" kg/m^2")

