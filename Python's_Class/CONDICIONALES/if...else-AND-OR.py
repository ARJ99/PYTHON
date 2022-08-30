           
#Short Hand If ... Else
#This technique is known as Ternary Operators, or Conditional Expressions.
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#AND
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#OR
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")  

#CHECK STRINGS
#IF .. IN ..
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#IF .. NOT IN ..
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")  







