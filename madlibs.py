print("welcome to the mad libs game!")
print("fill in the blanks to create your own funny story")

# Getting input from the user
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter a adjective: ")
place = input("Enter a place: ")

#Creating the story
story = f"Once upon a time, in a {adjective} {place}, she was a {noun} she {verb} the circek all the time."


# Display the funny story
print("\nhere is your mad libs story:")
print(story)

