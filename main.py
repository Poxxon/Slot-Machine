import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

#for slot machine reel
ROWS = 3
COLS = 3

#slot machine dictionary
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

#multipliers for each letter gotten in a row
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

#checks to see if three symbols are in one row
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        #get the symbol in the first index of the row
        symbol = columns[0][line]
        for column in columns:
            #check to see if the symbol matches the one at index 0
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

#to generate what symbols are gonna be each column based on the frequency of each symbol
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    #use symbols.items to get the symbols and their keys rather than looping through
    for symbol, symbol_count in symbols.items():
        #use _ for an undefined variable for usages in for loops to not have an unused variable in your program
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    #this loops picks a random value for each column 
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] #use [:] - slice operator to copy 
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    
    return columns

#using transposing to flip the columns 
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()



#responsible for collecting user input - gets deposit from user
#def = function
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        #to make sure the input is a digit
        if amount.isdigit():
            #covert string to int since the input that we asked for was a string
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount

#get the amount of lines the user would like to bet on (check constant value on the top to find out the value)
def get_number_of_lines():
    while True:
        lines = input("Enter the amount of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines!")
        else:
            print("Please enter a number.")

    return lines

#function to get the user's desired amount of bet on each line 
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                #use f to make it a f-string enabling inline usage of variables
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount

     
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You have insufficient funds to bet that amount. Your current balance is: ${balance}.")
        else:
            break
    
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to {total_bet}. ")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}!")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

#main function
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        prompt = input("Press enter to play (q to quit): ")
        if prompt == "q":
            break
        balance += spin(balance)

    print(f"You left with #{balance}")

#run the main program
main()


