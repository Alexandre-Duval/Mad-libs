import os

# words that the player will be asked to input
words = ["time of day", "place", "adjective", "animal", "noun", "adjective", "toy", "adjective"]

# list that will contain the answers the user inputs.
answers = []

# clears the terminal to make game more readable
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Function that welcomes player to mad lib game and produces the text after taking user input for each word.
def mad_lib():
    clear()
    while True:
        question = input("Welcome to Mad Libs! Would you like to play (y/n): ")
        if question == "y":
            for i in range(len(words)):
                user_input = input(f"{words[i]}: ")
                answers.append(user_input)
            template = f"{answers[0]}, I went to the {answers[1]} and found a {answers[2]} {answers[3]} hiding behind a {answers[4]}. It was so {answers[5]} that I couldn't resist taking it home. We spent the day together, playing with {answers[6]} and laughing until our stomachs hurt. It was the most {answers[7]} day ever!"
            print(template)
            print("\nThanks for playing!")
            break
        
        elif question == "n":
            print("Sorry to see you go.")
            break
        
        else:
            print("Invalid input.")


# Main funtion for mad lib game.
def main():
    mad_lib()

main()
