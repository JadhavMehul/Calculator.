print("\nhello \nWelcome to my calculator \n ")
print("What is your Calculator \n")
print("1 = Basic calculator \n2 = Area calculator \n3 = Factorial")

choice=int(input("\nEnter your Calculator = "))

if(choice==1):
    print("\nWow you have selected basic calculator \n")
    import Calculator

elif(choice==2):
    print("\nWow you have selected Area calculator \n")
    import Area

elif(choice==3):
    print("\nWow you have selected claculator to find Factorial \n")
    import Factorial

else:
    print("sorry, invalid choice")
