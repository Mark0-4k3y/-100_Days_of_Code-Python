#This is the fifth day of coding, in which I have to make an average height predictor application.

#First I have to take the list of heights of students.
heightList = input("Enter the height of the students in 'cm' separated by space:\n").split(' ')

#Now for finding the average of students height we have to do some calculations.
num = 0
for height in heightList:
    num = num + int(height)

print(round(num/len(heightList)))


#There is also another way to find out the sum of the list
#Python has inbuilt sum function which will return the sum of the list
numList = [150, 450, 850, 260, 2001]
print(sum(numList)/len(numList))