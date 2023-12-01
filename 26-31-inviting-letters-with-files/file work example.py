# Absolute file path
# with open("/Users/Abdi/Desktop/doc.txt", mode='r') as file:
#     print(file.read())

# using relative file path
with open("../../../Desktop/doc.txt") as file:
    print(file.read())
