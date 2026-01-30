# Code Requirements
# Input: Use any valid input source such as a keyboard, mouse, microphone, data stream, or file.
# Output: Must depend on the input provided.
# List Usage:
# Must justify why a list is better than alternatives.
# Examples include picking items, random selections, or using list methods like append.
# Function Requirements:
# Must have a parameter.
# Include sequencing (multiple lines of code).
# Utilize selection (e.g., if/else statements).
# Use iteration (e.g., loops like for or while).
# Take different paths based on parameter values.

joke = input("Do you want to hear a joke? Yes or No ")
if joke in ["Yes", "yes"]: #Added this so both an uppercase and lowercase yes would work
    print("Great, Do you want to hear a joke about robbers, tanks, or pencils?")
else:
    print("Okay, see you!")    
answer = input() # This turns the user's answer into a variable for use in the function below
jokes = ["robbers", "tanks", "pencils"]
def jokeys(answer):
    print("Knock Knock") # Added this line to initiate the joke and reuse it for all jokes
    if answer == jokes[0]:
        input("Calder")
        print("Calder police - I've been robbed!")
    elif answer == jokes[1]:
        input("Tank ")
        input("You are welcome! ")
    elif answer == jokes[2]:
        input("Broken pencil ")
        input("Nevermind, it's pointless! ")
    else:
        print("Sorry, I don't have a joke for that topic.") #This handles unexpected input
    
    
jokeys(answer) #This calls the function to run the joke based on user input
