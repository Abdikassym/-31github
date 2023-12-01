#TODO: Create a letter using starting_letter.txt

names = []


with open('Input/Names/invited_names.txt') as names_doc:
    people_name = names_doc.read()
    for name in people_name.split():
        names.append(name)
print(names)

file = open('Input/Letters/starting_letter.txt', "r")
starting_letter = file.read()

for name in names:
    with open(f"Output/ReadyToSend/letter_for_{name}", mode='w') as end_file:
        new_letter = starting_letter.replace("[name]", name)
        end_file.write(new_letter)
        print(new_letter)


#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp