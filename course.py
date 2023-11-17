import random


MAX_LINES = 3  #defining constant
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2,
    "B" : 8,
    "C" : 4,
    "D" : 6
}

#This means that if user wins any symbol below, wins 3,5,7,9 times their bet
symbol_value = {
    "A" : 3,
    "B" : 5,
    "C" : 7,
    "D" : 9
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][lines]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings = winnings + values[symbol] * bet
            winning_lines.append(lines + 1)

    return winnings, winning_lines


def get_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]   #copying all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns

def print_spin(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = " ¦ ")
            else:
                print(column[row], end = "")
        print()
def deposit():
    while True:
        amount = input("Enter deposit: £")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount should be greater than 0")
        else:
            print("Please enter a number")

    return amount


def get_no_of_lines():
    while True:
        lines = input("Enter number of lines(1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter valid number of lines")
        else:
            print("Please enter a number of lines: ")

    return lines

def get_bet():
    while True:
        amount = input("Enter bet for each line: £")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount should be between £{MIN_BET} - £{MAX_BET}")
        else:
            print("Please enter a number")

    return amount

def spin(balance):
    lines = get_no_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Not enough balance. Balance is: £{balance}")
        else:
            break
    print(f"you are betting £{bet} on {lines} lines. Total bet is £{total_bet}")

    slots = get_spin(ROWS, COLS, symbol_count)
    print_spin(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"you won £{winnings}")
    print(f"you won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is £{balance}")
        answer = input("Press enter to spin (q to quit)")
        if answer == "q":
            break
        balance = balance + spin(balance)
main()

