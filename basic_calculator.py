solution = 0
  if operator == "+":
    solution = num1 + num2
  if operator == "*":
    solution = num1 * num2
  if operator == "/":
    if num2 == 0:
      return"Can't divide by 0!"
    solution = num1 / num2
  if operator == "-":
    solution = num1 - num2
  return solution

