while True:
 try:
  num=list(map(float,input("Enter Two Numbers:").split()))
  print(num)

  if len(num)!=2:
   print("Please do not enter more than two numbers!!")
   raise ValueError
  break
 except ValueError:
  print("TrY AgAiN...!")

if(len(num)==2):
 operation=input("Select The Operator(+,-,*,/,%,//,**):")
 match operation:
  case '+':
   print(f"The Addition of Two Numbers is:{num[0]+num[1]}")
  case '-':
   print(f"The Substraction of Two Numbers is:{num[0]-num[1]}")
  case '*':
   print(f"The Multiplication of Two Numbers is:{num[0]*num[1]}")
  case '/':
   if(num[1]==0):
    print("Division by Zero is not possible")
   else:
    print(f"The Division of Two Numbers is:{num[0]/num[1]}")
  case '%':
   if(num[1]==0):
    print("Moduls by Zero is not possible")
   else:
    print(f"The Moduls of Two Numbers is:{num[0]%num[1]}")
  case '//':
   if(num[1]==0):
    print("Floor Division by Zero is not possible")
   else:
    print(f"The Floor Division of Two Numbers is:{num[0]//num[1]}")
  case '**':
   print(f"The Exponetial of Two Numbers is:{num[0]**num[1]}")
