x,y=map(float,input("Enter Two Numbers:").split())
operator=input("Select The Operator(+,-,*,/.%,//,**):")
if operator=='+':
	print(f"The result of Addition:{x+y}")
if operator=='-':
	print(f"The result of Subtraction is:{x-y}")
if operator=='*':
	print(f"The result of Multiplication is:{x*y}")
if operator=='/':
	if y==0:
		print("Division with zero is not Possible!!!")
	Selse:
		print(f"The result of Division is:{x/y}")
if operator=='%':
	if y==0:
		print("Modulo with zero is not Possible!!!")
	else:
		print(f"The result of Modulo is:{x/y}")
if operator=='//':
	if y==0:
		print("Floor Division with zero is not Possible!!!")
	else:
		print(f"The result of Floor Division is:{x/y}")
if operator=='**':
	print(f"The result of Exponential is:{x**y}")
