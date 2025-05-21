def calculator():
     #calculator function is used for calculate the give input
     num1=float(input("enter first number:"))
     operation=(input("enter operations(+,-,*,/,%)"))
     num2=float(input("enter second number:"))
    

     if operation=='+':
        result=num1+num2
     elif operation=='-':
        result=num1-num2
     elif operation=='*':
        result=num1*num2
     elif operation=='%':
        result=num1%num2
     elif operation=='/':
        if num2!=0:
             result=num1/num2
        else:
             print("0 is not divisible by any number")
             return
     else:
          print("invalid operation")
          return
     
     print("result",result)
calculator()

          
