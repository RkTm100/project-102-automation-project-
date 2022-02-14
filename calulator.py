
def add(x,y):
    return x+y

def substract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y



print("This is Raktim's Simple Automated Calculator")
print("______operations______")
print("1 - Add")
print("2 - substract")
print("3 - multiply")
print("4 - divide")
print("please type the number corresponding with the operation")
operation=input("Enter: ")

while True:

    if operation in ('1','2','3','4'):
        num1=input("Enter your first number: ")
        num2=input("Enter your second number: ")

        if operation=='1':
            print(num1+" + " + num2+ " = " + add(num1,num2))

        elif operation=='2':
            print(num1+ " - " + num2 + " = " + substract(num1,num2))

        elif operation=='3':
            print(num1+ " x " + num2 + " = " + multiply(num1,num2))

        elif operation=='4':
            print(num1 + " / " + num2 + " = " + divide(num1,num2))

        
        next_calc=input("do you want to do another calculation? Y/N")
        if next_calc=="N" or "n":
            break

    else:
        print("invalid input")



