# Add
def add(n1, n2):
  return n1 + n2

# Substract
def substract(n1, n2):
  return n1 - n2

# Multiply
def multiply(n1, n2):
  return n1 * n2

# Divide 
def divide(n1, n2):
  return n1 / n2

operations = {
  "+":add,
  "-":substract,
  "*":multiply,
  "/":divide,
}

n1 = int(input("Select a first number: "))

for operation in operations:
  print(operation)

operation_symbol = input("Pick an operation from a list above: ")

n2 = int(input("Select a second number: "))

operation_process = operations[operation_symbol]


print(operation_process(n1, n2))