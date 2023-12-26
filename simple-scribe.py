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


# Use the with open method to access create and write to a text file using
# a relative file path
with open("output.txt", "w+") as f:
    f.write(user_input + "\n")


def menu():
    print(
        "\033[0;30;47m\
    Underlined black text on a white background - BG_WHITE        \033[0m"
    )

    print(
        "\033[0;33;41m\
    Yellow text on a red background - BG_RED                      \033[0m"
    )

    print(
        "\033[30m\033[43m\
    Black text on a yellow background - BG_YELLOW                 \033[0m"
    )

    print(
        "\033[45m\
    White text on a magenta background - BG_MAGENTA               \033[0m"
    )

    print(
        "\033[30;46m\
    Black text on a cyan background - BG_CYAN                     \033[0m"
    )

    print(
        "\033[1;32;40m\
    Bold green text on a black background - BG_BLACK              \033[0m"
    )

    print(
        "\033[30m\n- FG_BLACK\033[0m"
        "\033[31m\n- FG_RED\033[0m"
        "\033[32m\n- FG_GREEN\033[0m"
        "\033[33m\n- FG_YELLOW\033[0m"
        "\033[34m\n- FG_BLUE\033[0m"
        "\033[35m\n- FG_MAGENTA\033[0m"
        "\033[36m\n- FG_CYAN\033[0m"
        "\033[37m\n- FG_WHITE\033[0m\n"
    )

    example = "Reverse your text?"
    print(example)
    example = "Reverse your text?"[::-1]
    print(example)
    print("\n\033[4mUnderline your text?\033[0m\n")


style_list = []


def edit_text(user_input):
    print(user_input)
    user_input = str(input("Please edit your text: "))
    return user_input


# Function which applies bold to the user input
def format_text(user_input, style_list):
    print(user_input)
    chosen_word = str(
        input(
            "Please type the text that you would like to apply styles to or enter / to edit your text: "
        )
    )

    menu()
    if chosen_word in user_input:
        styles = input("Please input the text style of your choice: ")
        if styles.lower() == "bold":
            styles = [BOLD]
        elif styles.lower() == "underlined":
            styles = [UNDERSCORE]
        edited_string = "".join(styles) + chosen_word + ALL_OFF
        user_input = user_input.replace(chosen_word, edited_string)
    elif chosen_word == "/":
        edit_text(user_input)

    format_text(user_input, style_list)


format_text(user_input, style_list)
