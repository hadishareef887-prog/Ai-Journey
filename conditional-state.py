age=int(input("Enter your age:"))
Gender=input("enter male or female:")
if(age>=21 and Gender=="male"):
    print("Can Vote and get a driving license.")
    print("Can also get Married.")

elif(18<=age<23 and Gender=="male"):
    print("Can Vote and get a driving license.")
    print("Cannot get Married.")

elif(age>=18 and Gender=="female"):
    print("Can Vote and get a driving license.")
    print("Can also get Married")

elif(age<18):
    print("Legally not allowed to Vote, Get a license, or get Married")

else:
    print("Please Enter a valid input")