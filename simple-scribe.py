# A program which will enable a user to input and edit text in a document
# that they create

while True:
    header = str(input("Please enter your header text here: "))
    body = str(input("Please enter your paragraph text here: "))
    footer = str(input("Please enter your footer text here: "))
    print(body, body, footer)
    break

# Use the with open method to access create and write to a text file using
# a relative file path
with open("output.txt", "w+") as f:
    f.write(body + "\n")

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
def bold(body):
    body = "\033[1m" + body + "\033[0m"
    print(body)
    body = "**" + "\033[1m" + body + "\033[0m" + "**"

    return body


# Function which applies italicised to the user input
def italicised(body):
    body = "\033[3m" + body + "\033[3m"
    print(body)
    body = "*" + "\033[1m" + body + "\033[0m" + "*"


# Function which applies capitalised to the user input
def capitalised(body):
    body = body.capitalize()
    print(body)
    body = f"{body} ## Capitalised"


# Function which applies underlined to the user input
def underlined(body):
    body = "".join([i + "\u0332" for i in body])
    print(body)
    body = f"{body} ## Underlined"

# Function which applies a default style to the header
def default_header(header):
    default_header = default_header.upper()
    default_header = "\033[1m" + default_header + "\033[0m"
    print(default_header)
    

    return default_header


# Function which calls another function depending on what text edit the user wants to apply
def edit_text():
    if editing_choice == "1":
        bold(body, )
    if editing_choice == "2":
        italicised(body)
    if editing_choice == "3":
        capitalised(body)
    if editing_choice == "4":
        underlined(body)


edit_text()
