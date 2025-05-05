#Asking user its name
from colorama import init, Fore, Style
init(autoreset=True)

name = input("What's your name, user? : ")
print(Fore.CYAN + f"\nWelcome to the Beast Calculator, {name}!")
print(Fore.YELLOW + "Where numbers crumble and math gets its revenge. 🔥💥")
print(Style.BRIGHT + Fore.MAGENTA + f"Get ready, {name}, it's time to unleash the power of math! 🚀")


#here are all the operations
def add(x: int, y: int) -> int:
    return f"Yoo {name}, the sum is {x + y}"

def sub(x: int, y: int) -> int:
    return f"Yoo {name}, the sub is {x - y}"

def mul(x: int, y: int) -> int:
    return f"Yoo {name}, the mul is {x * y}"

def div(x: int, y: int) -> int:
    if y == 0:
        raise ZeroDivisionError
    return f"Yoo {name}, the div is {x / y}"

#lets run our calculator here
def calc():

    operations = {
    "add": add,
    "sub": sub,
    "mul": mul,
    "div": div
}

    try:
        num1 = int(input(f"Enter first number {name}: "))
    except ValueError:
        print(f"Please enter a valid number {name}")
        return  # Exit the function if input is invalid

    try:
        num2 = int(input(f"Enter second number {name}: "))
    except ValueError:
        print(f"Please enter a valid number {name}")
        return  # Exit the function if input is invalid

    user_choice = input(f"What do you want to do {name}? (add, sub, mul, div): ").lower()
    
    try:
        if user_choice in operations:
            result = operations[user_choice](num1, num2)
            print(Fore.GREEN + f"Yoo {name}, the result is {result}")


        else:
            raise ValueError
    except ZeroDivisionError:
        print(Fore.RED + f"Bruhh {name} you tried to divide by zero 💀 Try again!")
    except ValueError:
        print(f"Yoo {name} please enter a valid operation dear...!!")

#asking if he/she wannause the calculator and repeat 
while True:
    calc()
    choice = input("Hey wanna use calculator 'yes' or 'no' :- ").lower()

    try:
        
        if choice == "no":
            print(f"Thank you {name} for using this calculator \n Hope it helps \n Have a great day")
            break
        elif choice != "yes":
            raise ValueError
    except ValueError:
        print(f"Yoo {name} plz enter 'yes' or 'no'. ")

        
    

        






