import random

MAX_LINES = 3 
MAX_BET = 100
MIN_BET = 1

SLOT_ROWS = 3
SLOT_COLS = 3

#dictionary 
symbol_count = {
    "A": 2,
    "B": 4, 
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 4,
    "B": 3,
    "C": 2,
    "D": 1
}

def check_winnings(columns, lines, bet, values): 
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns: 
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1) 
    return winnings, winning_lines
                

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows): 
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value) 
            
        columns.append(column)
    return columns

def print_slot_machine(columns):
    #transposing
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        
        print()
            

def deposit(): 
    while True:
        amount = input('how much would you like to deposit? $').strip()
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Amount must be greater than 0')
        else: 
            print('please enter a number')
    return amount 

def get_number_of_lines():
    while True:
        lines = input(f'Enter the number of lines to bet on (1- {str(MAX_LINES)})? ').strip()
        if lines.isdigit():
            lines = int(lines)
            if 0 < lines <= MAX_LINES:
                break
            else:
                print(f'Amount must be between 1 and{MAX_LINES}')
        else: 
            print('please enter a number')
    return lines
    
def get_bet(): 
    while True:
        amount = input('how much would you like to bet on each line? $')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f'Amount must be between ${MIN_BET} - ${MAX_BET}.')
        else: 
            print('please enter a number')
    return amount 

def game(balance):
    lines = get_number_of_lines()
    while True: 
        bet = get_bet() 
        total_bet = bet*lines
        if total_bet <= balance: 
            break
        else: 
            print(f'You do not have enough to bet that amount, your current balance is: ${balance}')
      
    print(f'You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}')
    slots = get_slot_machine_spin(SLOT_ROWS, SLOT_COLS, symbol_count)
    
    print_slot_machine(slots) 
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value) 
    print(f'You won ${winnings}')
    print(f'You won on lines: ', *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f'Current balance is ${balance}')
        spin = input('press enter to spin (q to quit)')
        if spin == 'q':
            break
        balance += game(balance)
        
    print(f'You left with ${balance}')
        
main() 