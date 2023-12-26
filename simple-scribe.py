# A program which will enable a user to input and edit text in a document
# that they create

while True:
    heading = str(input("Please enter your text here: "))
    body = str(input("Please enter your text here: "))
    footer = str(input("Please enter your text here: "))
    print(heading, body, footer)
    break

# Use the with open method to access create and write to a text file using
# a relative file path
with open("output.txt", "w+") as f:
    f.write(heading + "\n")

with open("output.txt", "r+") as f:
    for line in f:
        print(
            "\nThis is your text: "
            + line
            + "\nHow would you like to edit your text? Choose a number"
            + "\n\n1. Bold\n2. Italicised\n3. Capitalised\n4. Underlined\n"
        )

editing_choice = input("Please input the number of your choice: ")


# Function which applies bold to the user input
def bold(heading):
    heading = "\033[1m" + heading + "\033[0m"
    print(heading)
    heading = "**" + "\033[1m" + heading + "\033[0m" + "**"

    return heading


# Function which applies italicised to the user input
def italicised(heading):
    heading = "\033[3m" + heading + "\033[3m"
    print(heading)
    heading = "*" + "\033[1m" + heading + "\033[0m" + "*"


# Function which applies capitalised to the user input
def capitalised(heading):
    heading = heading.capitalize()
    print(heading)
    heading = f"{heading} ## Capitalised"


# Function which applies underlined to the user input
def underlined(heading):
    heading = "".join([i + "\u0332" for i in heading])
    print(heading)
    heading = f"{heading} ## Underlined"


# Function which calls another function depending on what text edit the user wants to apply
def edit_text():
    if editing_choice == "1":
        bold(heading, )
    if editing_choice == "2":
        italicised(heading)
    if editing_choice == "3":
        capitalised(heading)
    if editing_choice == "4":
        underlined(heading)


edit_text()
