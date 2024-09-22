## Variable Homework1 - Math Operation -- EASY
first = input('Enter first number: ')
first = float(first)

# let's make it in a single line
second = float(input('Enter second number: '))

print(first, '+', second, '=', first + second)
print(first, '-', second, '=', first - second)
print(first, '*', second, '=', first * second)
print(first, '/', second, '=', first / second)

print("\nEnd of program")
#--------------------------------------------------#


#---------------------------------------------------##
def compute_math(num1,num2, operator):
    if operator == '-' and num2 >= 0:
        return num1 - num2
    elif operator == '*' and num2 > 0:
        return num1 * num2
    elif operator == '/' and num2 >= 0:
        return num1 / num2
    elif operator == '+' and num2 >= 0:
        return num1 + num2
    else:
        print("Please check your values, must be positive  numbers only")


print(compute_math(10, 5, '+'))  # Addition
print(compute_math(10, 5, '-'))  # Subtraction
print(compute_math(10, 5, '*'))  # Multiplication
print(compute_math(10, 5, '/'))  # Division

#==========================================================================#
#Problem2

student_name1 = input("Enter the first student's Name : ")
student_id1 = input("Enter the first student's ID : ")
student_grade1 = int(input("Enter the first student's grade : "))
student_name2= input("Enter the first student's Name : ")
student_id2 = input("Enter the first student's ID : ")
student_grade2 = int(input("Enter the first student's grade : "))
print(f"{student_name1}({student_id1}) got grade : {student_grade1}")
print(f"{student_name2}({student_id2}) got grade : {student_grade2}")
print(f"Average Math Grade is {(student_grade1 + student_grade2)/2}")

    #------------------------------------------------------#
name1 = input("Enter the first stduent's name: ")
id1 = input("Enter the first stduent's ID: ")
grade1 = float(input("Enter the first stduent's grade: "))

name2 = input("\nEnter the second stduent's name: ")
id2 = input("Enter the second stduent's ID: ")
grade2 = float(input("Enter the second stduent's grade: "))

print('\n\nInformat for students and their "Math" grades')
msg = name1 + '(ID ' + id1 + ') got grade: ' + str(grade1)
print(msg)
msg = name2 + '(ID ' + id2 + ') got grade: ' + str(grade2)
print(msg)

average = (grade1 + grade2) / 2.0
print('Average math grade is', average)
###############################################################################
list1 = [11,2,7,9,12,-8,3,-1]
even_count= 0
odd_count=0
for i in range(list1):
    if i%2 == 0:
        even_count+=i
    else:
        odd_count+=i
#--------------------------------------------------------#
A = input()
B = input()
C = input()

combo = A + "'" + B + '"' + C
combo = combo * 10

print(combo)
#-------------------------------------------------------#

# twp solutions to swap values between two numbers
num1 = 25
num2 = 34
num1,num2= num2,num1
print(f" num1 is : {num1}, and num2 is {num2}")

num1 = 100
num2 = 657
tmp = num1
num1 =num2
num2 = tmp
print(f" num1 is : {num1}, and num2 is {num2}")
#------------------------------------------------##
## HARD PROBLEMS -Swapping Three Numbers
num1,num2,num3 = map(int,input().split())
tmp1 = num1 #10
num1 = num2
num2 = num3
num3 = tmp1
print(f" num1 is : {num1}, and num2 is {num2} and num3 is {num3}")
#===========================================================#
a, b = map(int, input().split())
if b < 0:
    print(2 * a + 1)
else:
    print(a * a)
#=======================================++++++#
