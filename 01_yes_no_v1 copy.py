
show_instructions = ""
while show_instructions.lower() != "xxx":
    # ask the user if they have played before
    show_instructions = input("Have you played this game before? ").lower()

    # if yes, output 'program continues'
    if show_instructions == "yes" or show_instructions == "y":
        show_instructions = "yes"
        print("program continues")

    # if no, output 'display instructions'
    elif show_instructions == "no" or show_instructions == "n":
        show_instructions = "no"
        print("display instructions")

    # if invalid, print please answer yes or no
    else:
        print("Please answer yes / no")
