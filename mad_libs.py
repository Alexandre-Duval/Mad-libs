words = ["time of day", "place", "adjective", "animal", "noun", "adjective", "toy", "adjective"]

mad_lib = f"{words[0]}, I went to the {words[1]} and found a {words[2]} {words[3]} hiding behind a {words[4]}. It was so {words[5]} that I couldn't resist taking it home. We spent the day together, playing with {words[6]} and laughing until our stomachs hurt. It was the most {words[7]} day ever!"

# Takes in user input for every word in the words list and prints the completed text. 
def user_input(words: list):
    input("Welcome to the mad libs program!\n")
    for word in words:
        while True:
            answers = input(f"{word}: ")
            if type(answers) == str:
                word = answers
                break
            else: 
                continue
    print(mad_lib)

# Main function of program
def main():
    user_input(words)

main()
