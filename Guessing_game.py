from random import choice
from csv import DictReader



def read_quotes(filename):
    with open(filename, "r", encoding='utf-8', newline='') as file:
        csv_reader = DictReader(file)
        quotes = list(csv_reader)
        return quotes
link = "http://quotes.toscrape.com"
quotes = read_quotes("quotes.csv")



def start_game(quotes):
    random_quote = choice(quotes)
    guesses = 4
    print("Here's a quote: ")
    print(" ")
    print(random_quote["text"])
    user_input = ''
    while user_input.lower() != random_quote["author"].lower() and guesses > 0:
        user_input = input(f"Who said this? Guesses remaining {guesses}: ")         
        if user_input.lower() == random_quote["author"].lower():
            print("Congratulations! You won.")                        
        elif guesses == 4:
            print(f"Here's a hint: The author was born on {get_author_birt_date(link+random_quote['bio_link'])} {get_author_birt_place(link+random_quote['bio_link'])}")
            guesses -= 1
            continue
        elif guesses == 3:
            print(f"Here's a second hint: The author name starts with {random_quote['author'][0]}")
            guesses -= 1
            continue
        elif guesses == 2:
            print(f"Here's the final hint: The author initials are {random_quote['author'].split()[0][0] + '.' + random_quote['author'].split()[1][0] + '.'}")
            guesses -= 1
            continue
        elif guesses == 1:
            print(f"No more quesses remaining. The author's name is {random_quote['author']}")
            guesses -=1
    ask = ''
    while ask.lower() not in ("yes", "y", "n", "no"):
        ask = input("Wanna play again? y/n:")
        if ask.lower() in ("yes", "y"):
            return start_game(quotes)
        else:
            print("Ok. Goodbye!")
            

            
        
    
start_game(quotes)
