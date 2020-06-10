from random import choice
from csv import DictReader

def quotes_reader(filename):
    with open(filename, "r", encoding = "utf-8", newline = "") as file:
        csv_reader = DictReader(file)
        quotes = list(csv_reader)
        return quotes

if __name__ == '__main__':
    quotes = quotes_reader("Quotes.csv")

def start_game(quotes):
    random_quote = dict(choice(quotes))
    print('')
    print('')
    print('')
    print("Here's a quote:")
    print(" ")
    print(random_quote["text"])
    print('')
    guesses = 4
    while True:
        user_input = input("Who said this? : ")
        guesses -= 1
        if user_input.lower() == random_quote["author"].lower():
            print("Congratulations! You won")
            break
        elif user_input.lower() != random_quote["author"].lower():
            if guesses == 3:
                print("Ooops. Try again!")
                print(f"Here's a hint: The author was born in {random_quote['birthplace']}")
            elif guesses == 2:
                print("Ooops. Try again!")
                print(f"Here's a hint: The author name starts with {random_quote['author'][0]}")     
            elif guesses == 1:
                print("Ooops. Try again!")
                print(f"Last hint: The author initials are {random_quote['author'].split(' ')[0][0] + '.' +  random_quote['author'].split(' ')[1][0] + '.'}")               
            elif guesses == 0:
                print(f"Ooops. The name of the author is {random_quote['author']}")
                break
    play_again = str(input("Wanna play again? y/n: "))
    while play_again.lower() not in ("yes","y", "n", "no"):
        print("Please input yes or no.")
        play_again = str(input("Wanna play again? y/n: "))
    if play_again.lower() in ("yes","y"):
        print('')
        print('')
        start_game(quotes)
    else:
        print('')
        print('')
        print('Ok. Goodbye!')
        
if __name__ == '__main__':
    start_game(quotes) 