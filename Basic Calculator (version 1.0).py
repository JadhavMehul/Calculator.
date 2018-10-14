
def calc_add(a,b):
        return a+b
def calc_sub(a,b):
        return a-b
def calc_float_div(a,b):
        return a/b
def calc_int_div(a,b):
        return a//b
def calc_multi(a,b):
        return a*b
def calc_square(a,b):
        return a**b

print("1 = addition \n 2 = subtraction \n 3 = float division \n"
      "4 = intiger division \n 5 = multiply \n 6 = square")

choice=int(input("enter your choice="))
a=int(input("enter a number"))
b=int(input("enter a number"))


if(choice==1):
    print("the addition of",a,"and",b,"=",calc_add(a,b,c))

elif(choice==2):
    print("the addition of",a,"and",b,"=",calc_sub(a,b))

elif(choice==3):
    print("the addition of",a,"and",b,"=",calc_float_div(a,b))

elif(choice==4):
    print("the addition of",a,"and",b,"=",calc_int_div(a,b))

elif(choice==5):
    print("the addition of",a,"and",b,"=",calc_multi(a,b))

elif(choice==6):
    print("the addition of",a,"and",b,"=",calc_square(a,b))

else:
    print("sorry you selected a choice which is not mention")
