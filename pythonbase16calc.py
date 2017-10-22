import os

def calculator(num1,num2,calctype):
    no1 = int(num1,16)
    no2 = int(num2,16)
    if calctype == 1:
        b10 = no1 + no2
        return hex(b10)
    elif calctype== 0:
        if no1 > no2:
            b10 = no1 - no2
            return hex(b10)
        else:
            b10 = no2 - no1
            return hex(b10)
        
def validateNum(num):
    try:
        int(num, 16)
        return 0
    except ValueError:
        print("Unvalid Base16 number.")
        return 1
        
exitcode = 0
print("For help use the 'help' command.")
while exitcode == 0:
    inputvalid = 0
    num1valid = 0
    num2valid = 0
    cmdreturn = 0
    while cmdreturn == 0:
        baseinput = input("Awaiting for user input...")
        if baseinput == "exit" or baseinput == "quit" or baseinput == "q":
            exitcode = 1
            raise SystemExit
        elif baseinput == "clear" or baseinput == "cls" or baseinput == "c":
            os.system("cls")
        elif baseinput == "help" or baseinput == "h":
            print ("Commands:")
            print ("Exiting the program: 'exit' 'quit' 'q'")
            print ("Clearing the screen: 'clear' 'cls' 'c'")
            print ("Help: 'help' 'h'")
        else:
            cmdreturn = 1
        
        
    uinput = input("Select the calculation type (+/-):")
    while inputvalid == 0:
        if uinput == "-":
            inputvalid = 1
        elif uinput == "+":
            inputvalid = 1
        else:
            print("Unvalid calculation type.")
            uinput = input("Select the calculation type (+/-):")
            
    uinput1 = input("Number1: ")
    while num1valid == 0:
        val = validateNum(uinput1)
        if val == 0:
            num1valid = 1
        else:
            uinput1 = input("Number1: ")

    uinput2 = input("Number2: ")
    while num2valid == 0:
        val = validateNum(uinput2)
        if val == 0:
            num2valid = 1
        else:
            uinput1 = input("Number2: ")
    print()
    print("Result:")
    if uinput == "-":
        result = calculator(uinput1, uinput2, 0).upper()
        fixedresult = result.replace("0X", "")
        print(fixedresult)
    elif uinput == "+":
        result = calculator(uinput1, uinput2, 1).upper()
        fixedresult = result.replace("0X", "")
        print(fixedresult)
    print()
