#basic calculator program in idle python 

def calc_add(a,b): #function to calculate addition
        return a+b #formula of addition

def calc_sub(a,b): #function to calculate subtraction
        return a-b #formula of subtraction

def calc_float_div(a,b): #function to calculate float division i.e if number is 2 then output is 2.0
        return a/b #formula of float division

def calc_int_div(a,b): #function to calculate integer division i.e if number is 2.0 then output is 2
        return a//b #formula of int division

def calc_multi(a,b): #function to calculate multiplication
        return a*b #formula of multilication

def calc_square(a,b): #function to calculate to do square
        return a**b #formula of square

while True:
        print("1 = addition \n"
              "2 = subtraction \n"
              "3 = float division \n"
              "4 = intiger division \n"
              "5 = multiply \n 6 = square")
        choice=int(input("enter your choice="))
        a=int(input("enter a number"))
        b=int(input("enter a number"))

        if(choice==1):
                print("the addition of",a,"and",b,"=",calc_add(a,b),"\n")

        elif(choice==2):
                print("the subtraction of",a,"and",b,"=",calc_sub(a,b),"\n")

        elif(choice==3):
                print("the float division of",a,"and",b,"=",calc_float_div(a,b),"\n")

        elif(choice==4):
                print("the integer division of",a,"and",b,"=",calc_int_div(a,b),"\n")

        elif(choice==5):
                print("the multiplication of",a,"and",b,"=",calc_multi(a,b),"\n")

        elif(choice==6):
                print(a,"to the power",b,"=",calc_square(a,b),"\n")
        
        elif(choice==0): break
                
        else:
                print("sorry you selected a choice which is not mention")
                
