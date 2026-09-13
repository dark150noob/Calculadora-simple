print("********************")
print("*Calculadora Simple*")
num1=int(input("********************\n"))
while True:
    op=input()
    num2=int(input())

    if op=="+":
        num1+=num2
        print(round(num1, 2))
        continue
    elif op=="-":
        num1-=num2
        print(round(num1, 2))
        continue
    elif op=="*":
        num1*=num2
        print(round(num1, 2))
        continue
    elif op=="/":
        num1/=num2
        print(round(num1, 2))
        continue
    elif op=="//":
            num1//=num2
            print(round(num1, 2))
            continue
    elif op=="%":
            num1%=num2
            print(round(num1, 2))
            continue
    elif op=="**":
            num1**=num2
            print(round(num1, 2))
            continue
    else:
        print("Esa opción no está contemplada.")
        break
    
