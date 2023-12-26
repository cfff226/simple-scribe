from __future__ import print_function

# Special END separator
END = "0e8ed89a-47ba-4cdb-938e-b8af8e084d5c"

# Text attributes
ALL_OFF = "\033[0m"
BOLD = "\033[1m"
UNDERSCORE = "\033[4m"
BLINK = "\033[5m"
REVERSE = "\033[7m"
CONCEALED = "\033[7m"

# Foreground colors
FG_BLACK = "\033[30m"
FG_RED = "\033[31m"
FG_GREEN = "\033[32m"
FG_YELLOW = "\033[33m"
FG_BLUE = "\033[34m"
FG_MAGENTA = "\033[35m"
FG_CYAN = "\033[36m"
FG_WHITE = "\033[37m"

# Background colors
BG_BLACK = "\033[40m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"


# A program which will enable a user to input and edit text in a document
# that they create

list_of_strings = []

user_input = str(input("Please enter your text here: "))
list_of_strings.append(user_input)
print(list_of_strings)
print(user_input)


# Use the with open method to access create and write to a text file using
# a relative file path
with open("output.txt", "w+") as f:
    f.write(user_input + "\n")


# Function which applies bold to the user input
def format_text(user_input, list_of_strings):
    chosen_word = str(
        input("Please type the text that you would like to apply styles to: ")
    )
    if chosen_word in user_input:
        styles = [BOLD, BG_GREEN, UNDERSCORE]
        edited_string = "".join(styles) + chosen_word + ALL_OFF
        user_input = user_input.replace(chosen_word, edited_string)
        print(user_input)


format_text(user_input, list_of_strings)
