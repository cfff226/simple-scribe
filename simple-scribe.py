# A program which will enable a user to input and edit text in a document
# that they create

user_input = str(input("Please enter your text here: "))


# Use the with open method to access create and write to a text file using
# a relative file path
with open("output.txt", "w+") as f:
    f.write(user_input + "\n")

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
def bold(user_input):
    user_input = "\033[1m" + user_input + "\033[0m"
    print(user_input)
    user_input = "**" + "\033[1m" + user_input + "\033[0m" + "**"

    return user_input


# Function which applies italicised to the user input
def italicised(user_input):
    user_input = "\033[3m" + user_input + "\033[3m"
    print(user_input)
    user_input = "*" + "\033[1m" + user_input + "\033[0m" + "*"


# Function which applies capitalised to the user input
def capitalised(user_input):
    user_input = user_input.capitalize()
    print(user_input)
    user_input = f"{user_input} ## Capitalised"


# Function which applies underlined to the user input
def underlined(user_input):
    user_input = "".join([i + "\u0332" for i in user_input])
    print(user_input)
    user_input = f"{user_input} ## Underlined"


# Function which calls another function depending on what text edit the user wants to apply
def edit_text():
    if editing_choice == "1":
        bold(user_input)
    if editing_choice == "2":
        italicised(user_input)
    if editing_choice == "3":
        capitalised(user_input)
    if editing_choice == "4":
        underlined(user_input)


edit_text()
