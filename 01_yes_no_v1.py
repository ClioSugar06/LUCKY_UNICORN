# ask if the user has played before
show_instructions = input("Have you played this game before?") .lower()

# if yes, output 'program continues'
if show_instructions == "yes" or "y":
    print("program continues")

elif show_instructions == "no" or "n":
    print("display instructions")

# if no, output 'display instructions'
else:
    print("Please answer yes / no")
