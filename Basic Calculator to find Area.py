#python program to calculate area

def calc_area_circle():#function to calculate area of circle
    pie=3.14
    radius=int(input("enter value of radius="))#user input value of radius
    formula=pie*(radius*radius)#formula to calculate area of circle
    return formula

def calc_area_rectangle():#function to calculate area of rectangle
    length=int(input("enter value of length="))#user input value of length
    breath=int(input("enter value of breath="))#user input value of breath
    formula=length*breath#formula to calculate area of rectangle
    return formula

def calc_area_square():#function to calculate area of square
    side=int(input("enter value of side="))#user input value of side
    formula=side*side#formula to calculate area of square
    return formula

def calc_area_triangle():#function to calculate area of triangle
    base=int(input("enter value of base="))#user input value of base
    height=int(input("enter value of height="))#user input value of height
    formula=(base*height)/2#formula to calculate area of triangle
    return formula

while True:
    print("select your choice \n"
          "1 = area of circle \n"
          "2 = area of rectangle \n"
          "3 = area of square \n"
          "4 = area of triangle")#output
    c=int(input("enter your choice="))#user input c=choice

    if(c==1):
        print("area of circle =",calc_area_circle(),"\n")

    elif(c==2):
        print("area of rectangle =",calc_area_rectangle(),"\n")

    elif(c==3):
        print("area of square =",calc_area_square(),"\n")

    elif(c==4):
        print("area of triangle =",calc_area_triangle(),"\n")

    elif(a==0): break

    else:
        print("sorry you selected a choice which is not mention")


