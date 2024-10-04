for counter in range(1,22):
    if counter % 2 == 0:
        print(f"{counter} is even" )
        continue
    print(f"{counter} is odd")
#=============================


for num in range(20):
    if num % 3 == 0:
        print(f"{num} is divisible by 3")

else:
    print(num)


def reverse_fn(word):
    char = ' '
    for i in word:
        char = i + char
   
    return char



print(reverse_fn("MAF"))


#=================================
pi = 3.14
r = int(input("Enter the Radius :"))
area_circle = pi * r**2
circum_circle = 2 * pi * r 
print(area_circle, circum_circle) 
#===================================
special_char = ['!','@','#','$','%','^','&','*','(',')']

user_name = input("Enter your name without any special character")
for i in user_name:
    if special_char in user_name:
        print("you typed your name with a special character")
    else:
        user_email = input("please enter your email :")
        break


        

print(user_name, user_email)  

special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

user_name = input("Enter your name without any special character: ")

# Check if the name contains any special characters
contain_special_char = False
for char in user_name:
    if char in special_chars:
        contain_special_char=True
        break
if contain_special_char:
    print("you typed your name with special char")
else:
    user_email = input("Enter your email :")
    print(user_name, user_email)    




def factorial(num):
    if num == 0:
        return 1
    else:

        return num * factorial(num -1)


print(factorial(5))



#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
#Sample value of n is 5

n = int(input("Enter the number : "))
print(n+(n*n)+ (n*n*n))


n = int(input("Enter an integer (n): "))
nn = int(str(n) + str(n))
nnn = int(str(n) + str(n) + str(n))

result = n + nn + nnn

print(f"The result of {n} + {nn} + {nnn} is: {result}")





a = 10 
b = 12
a = a + b
b = a -b
a = a - b
print( "a :", a, "b equal :", b )
