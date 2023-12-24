# A program which will enable a user to input and edit text in a document
# that they create


user_input = str(input("Please enter your text here: "))

# Use the with open method to access create and write to a text file using
# a relative file path
with open("output.txt", "w") as f:
    f.write(user_input + "\n")
