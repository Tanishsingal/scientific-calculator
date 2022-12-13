print("\t___Calculator___")
def A_d(a,b):
    print("Sum is ",a+b)
def S_b(a,b):
    if a>b:
        print("Differnce is",a-b)
    else:
        print("Differnce is",b-a)
def M_l(a,b):
    print("Product is",a*b)
import math
def chin_chong(a):
    print("The square root of this number is ",math.sqrt(a))
def radian(a):
    print("radian of angle is",math.radians(a))
def sin(a):
    print("sin of angle is",math.sin(math.radians(a)))
def cos(a):
    print("cos of angle is",math.cos(math.radians(a)))
def tan(a):
    print("tan of angle is",math.tan(math.radians(a)))
def pow(a,b):
    print("power of nunmber is",math.pow(a,b))
while(True):
    print("Please Enter the operation need to be performed\n 1) Addition \n 2) Substraction \n 3) Multiplication \n 4) Square Root of Number \n 5) radian of a number \n 6) sin of a number \n 7) cos of a number \n 8) tan of a number \n9)exit")
    print("You can enter the \'Number' of operation which you need to be performed")
    o=int(input("Please Enter your operation number\n"))
    if o==1:
        a=int(input("Enter the number\'1'\n"))
        b=int(input("Enter the number\'2'\n"))
        A_d(a,b)
        pass
    elif o==2:
         a=int(input("Enter the number\'1'\n"))
         b=int(input("Enter the number\'2'\n"))
         S_b(a,b)
    elif o==3:
        a=int(input("Enter the number\'1'\n"))
        b=int(input("Enter the number\'2'\n"))
        M_l(a,b)
    elif o==4:
        a=int(input("Enter the number\n"))
        chin_chong(a)
    elif o==5:
        a=int(input("Enter the degree\n"))
        radian(a)
    elif o==6:
        a=int(input("Enter the degree\n"))
        sin(a)
    elif o==7:
        a=int(input("Enter the degree\n"))
        cos(a)
    elif o==8:
        a=int(input("Enter the degree\n"))
        tan(a)
    elif o==9:
        print("Adio\'s Amigo\'s \n 'Byee..!'")
        break
    else:
        print("The Number Entered is out of range")