a=int(input("enter a number="))
factorial = 1
if a <= 0:
    print("factorial of {} does not exist".format(a))

else:
    for i in range(1,a+1):
        factorial=factorial*i
    print("factorial of {} is {}".format(a,factorial))
