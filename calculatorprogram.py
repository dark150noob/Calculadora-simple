print("********************")
print("*Calculadora Simple*")
num1=int(input("********************\n"))

if num1==int:
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
                print("esa opción no está contemplada")
                break
else:
        print("Recuerde introducir un valor entero")    


    
