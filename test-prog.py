# num=int(input("Enter the number:"))
# quo=num%2
# if(quo==0):
#     print("The given number is an Even number.")
# else:
#     print("The given number is an Odd number.")

#Executed properly, hence commented out

num1=int(input("Enteer the 1st number:"))
num2=int(input("Enteer the 2nd number:"))
num3=int(input("Enteer the 3rd number:"))
if (num1>num2 and num1>num3 ):
    high=num1
elif(num2>num1 and num2>num3):
    high=num2
else:
    high=num3

print("Largest number of the provided numbers is:", high)