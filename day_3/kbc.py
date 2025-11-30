print("********************  Welcome To KBC  ********************")
print("Here is a chance to WIN BIG amount of 15,000/- Rs.")
print("Simply answer 15 easy Questions to win the Prize amount")
play_tuple=('yes','no')
while True:
 play=input("Would You Like To Play 'Yes or No':").lower()
 try:
  if play not in play_tuple:
   raise ValueError
  break
 except ValueError:
  print("Enter correct option 'Yes' or 'No'...!!")
  print("Please Try Again...!!")
if play=="no":
 print("Thank You for the Responce....Enjoy Your Day...!!")
elif play=="yes":
 print("Great Choice...All the best for your Game")
 ql=[
"Q1. Python file extension is: A. .pt B. .py C. .pyt D. .python",
"Q2. Function to display output: A. echo() B. output() C. print() D. display()",
"Q3. Valid variable name: A. 2name B. my-name C. my_name D. my name",
"Q4. Data type for True/False: A. String B. Boolean C. Integer D. Float",
"Q5. Symbol for comments in Python: A. // B. <!-- C. '#' D. /* ",
"Q6. Output of len('Python'): A. 5 B. 6 C. 7 D. 0",
"Q7. Which is a list? A. {1,2,3} B. (1,2,3) C. [1,2,3] D. <1,2,3>",
"Q8. Keyword to define a function: A. func B. define C. def D. function",
"Q9. Result of 3 == 3: A. 3 B. False C. True D. Error",
"Q10. Exponent operator: A. ^ B. ** C. * D. ^^",
"Q11. Convert string to integer: A. int() B. str() C. float() D. number()",
"Q12. Which is a dictionary? A. [1:'a'] B. {1:'a'} C. (1:'a') D. <1:'a'>",
"Q13. Result of type(5): A. float B. str C. bool D. int",
"Q14. Keyword for error handling: A. catch B. try C. error D. throw",
"Q15. Output of 2 + 3 * 4: A. 20 B. 14 C. 24 D. 18"
]
 al=["b","c","c","b","c","b","c","c","c","b","a","b","d","b","b"]
 i=0
 PRIZE=0
 while True:
  if(i<15):
   print(ql[i])
   ans=input("Enter Your Desired Option from 'A , B , C , D':").lower()
  if(i==15):
   print(f"Your winning Ammount is:{PRIZE}")
   break
  elif(ans==al[i]):
   i+=1
   PRIZE+=1000
   if(i<14):
    print("Congratulations...Keep Up The Winning Streak")
   else:
    print("Congratulations...You have answered all the Question Correctly")
  else:
   print("Sorry but that is a WRONG ANSWER...Better Luck Next Time...!!!")
   print(f"Your winning Prize is:{PRIZE}")
