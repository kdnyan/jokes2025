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

jokes = ["robbers", "tanks", "pencils"] # we create a list at the start to store joke topics

def tell_joke(answer):
    print("Knock Knock") #we moved the common "Knock Knock" line outside the selection structure to avoid repetition
    if answer == jokes[0]: #we use the list to access joke topics instead of typing them out multiple times, and since theres only 3 options, this is more efficient
        input("Calder") 
        print("Calder police - I've been robbed!") #we removed unnecessary input prompts that did not contribute to the joke  
    elif answer == jokes[1]:
        input("Tank ")
        print("You are welcome! ") #we removed unnecessary input prompts that did not contribute to the joke 
    elif answer == jokes[2]:
        input("Broken pencil ")
        print("Nevermind, it's pointless! ") #we removed unnecessary input prompts that did not contribute to the joke 
    else:
        print("Sorry, I don't have a joke for that topic.")  #we added an else statement to handle unexpected inputs and simplify the code structure

joke = input("Do you want to hear a joke? Yes or No ") 
while joke in ["Yes", "yes"]: # we use a list to check for multiple acceptable inputs for yes
    print("Great, Do you want to hear a joke about robbers, tanks, or pencils?")
    answer = input()
    tell_joke(answer)
    joke = input("Do you want to hear another joke or are you finished? ")

print("Okay, see you!")
rate = int(input("Please rate our game 1-10! ")) #instead of asking for rating only if finished, we ask it always after exiting the joke loop
final_score = int(rate * 10)
print(str(final_score) + " percent satisfaction rate") 

friend = input("Would you recommend this game to a friend? ") 
if friend in ["yes", "maybe"]: # we created a list of acceptable answers for recommending the game instead of relying on multiple or conditions like or 
    print("Thanks, we appreciate it. ")
else:
    print("Sorry you did not enjoy it. ")
