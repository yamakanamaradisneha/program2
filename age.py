try:
  age=int(input("Enter age:"))
  if age >= 20:
    print("Not eligible to vote")
  else:
    print("Not eligible to vote")
except ValueError:
  print(f" Enter a valid age")
