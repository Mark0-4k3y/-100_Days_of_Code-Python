#This is the second project of day 5, in which I have to find and return the maximum score from the student subjects.

#First I will have to take the subject name and the marks of respective subject as input
subList = input('Enter the name of subjects separated by space: \n').split(' ')
marksList = []
for subject in subList:
    marksList.append(int(input(f"Enter the marks of the {subject}: ")))

maxMarks = marksList[0]
index = 0
sub = 0
for marks in marksList:
    if marks > maxMarks:
        maxMarks = marks
        sub = index
    index += 1

print(f'The student have maximum marks in {subList[sub]}, which are: ', maxMarks, '\n')

#What if the student have same maximum marks in more than one subject
indexList = []
index = 0
for mark in marksList:
    if maxMarks == mark:
        indexList.append(index)
    index += 1

print("The students have maximum marks in more than one subject which are: ")
for i in indexList:
    print(subList[i], end=', ')
print(f"and the maximum marks is: {maxMarks}")


#There are also inbuilt function in python which will return maximum and minimum value
print(max(marksList), " and", min(marksList))