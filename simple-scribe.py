from __future__ import print_function

# A program which will enable a user to input and edit text in a document
# that they create

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


user_input = str(input("Please enter your text here: "))


# Use the with open method to access create and write to a text file using
# a relative file path
with open("output.txt", "w+") as f:
    f.write(user_input + "\n")


def menu():
    print(
        "\n\033[0;30;47m\
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
    print("Type 'Reversed'")
    print("\n\033[4mUnderline your text?\033[0m")
    print("Type 'Underlined'")
    print("\nStandard text with no style? Type 'Clear'\n")

# Function which enables the user to re write their text
def edit_text(user_input):
    print(f"\n\n{user_input}\n\n")
    user_input = str(input("Please edit your text: "))
    format_text(user_input)
    return user_input


# Function which applies styles to the user input
def format_text(user_input):
    print(f"\n\n{user_input}\n\n")
    chosen_word = str(
        input(
            "Please type the text that you would like to apply styles, enter / to edit your text or enter - to exit: "
        )
    )
    menu()
    if chosen_word in user_input:
        styles = input("\nPlease input the text style of your choice: ")
        if styles.lower() == "bold":
            styles = [BOLD]
        elif styles.lower() == "underlined":
            styles = [UNDERSCORE]
        elif styles.lower() == "clear":
            styles = [ALL_OFF]
        elif styles.lower() == "fg_black":
            styles = [FG_BLACK]
        elif styles.lower() == "fg_red":
            styles = [FG_RED]
        elif styles.lower() == "fg_green":
            styles = [FG_GREEN]
        elif styles.lower() == "fg_yellow":
            styles = [FG_YELLOW]
        elif styles.lower() == "fg_blue":
            styles = [FG_BLUE]
        elif styles.lower() == "fg_magenta":
            styles = [FG_MAGENTA]
        elif styles.lower() == "fg_cyan":
            styles = [FG_CYAN]
        elif styles.lower() == "fg_white":
            styles = [FG_WHITE]
        elif styles.lower() == "bg_black":
            styles = [BG_BLACK]
        elif styles.lower() == "bg_red":
            styles = [BG_RED]
        elif styles.lower() == "bg_green":
            styles = [BG_GREEN]
        elif styles.lower() == "bg_yellow":
            styles = [BG_YELLOW]
        elif styles.lower() == "bg_blue":
            styles = [BG_BLUE]
        elif styles.lower() == "bg_magenta":
            styles = [BG_MAGENTA]
        elif styles.lower() == "bg_cyan":
            styles = [BG_CYAN]
        elif styles.lower() == "bg_white":
            styles = [BG_WHITE]
        else:
            print(
                "\n -------------- Your choice has not been recognised --------------\n"
            )
            format_text(user_input)

        edited_string = "".join(styles) + chosen_word + ALL_OFF
        user_input = user_input.replace(chosen_word, edited_string)
    elif chosen_word == "/":
        edit_text(user_input)
    elif chosen_word == "-":
        print(user_input)
        quit()

    format_text(user_input)


format_text(user_input)
