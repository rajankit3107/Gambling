import random




MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 10

ROWS = 3
COLS = 3

symbol_count = {
     "A": 2,
     "B": 4,
     "C": 6,
     "D": 8,
}

symbol_values = {
     "A": 5,
     "B": 4,
     "C": 3,
     "D": 2,
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
     for _ in range(cols):
         column = []
         current_symbols = all_symbols[:]
         for _ in range(rows):
              value = random.choice(current_symbols)
              current_symbols.remove(value)
              column.append(value)

         columns.append(column)

     return columns

def print_slot_machine(columns):
     for row in range(len(columns[0])):
         for i, column in enumerate (columns):
             if i !=len(columns) - 1:
                print(column[row], end="|")
             else:
                print(column[row])

  
   

def deposit():
    while True:
        amount = input("Enter amount to deposit: $")

    
        if(amount.isdigit()): # Checks if the input is a number
            amount = int(amount)  # Converts the input to an integer

            

            if(amount > 0):
            
                break
            else:

                print("Please enter a positive number.")

              

        else:
                
                print("Please enter a number.")
        






    return amount




def get_number_of_lines():
    while True:
        lines = input("Enter number of lines to play: ")
        if(lines.isdigit()): # Checks if the input is a number
            lines = int(lines)  # Converts the input to an integer

            

            if(lines > 0 and lines <= MAX_LINES):
            
                break
            else:

                print("Please enter a valid number.")

        else:
                
                print("Please enter a number.")

    return lines

def get_bet_amount():
    while True:
        bet = input("Enter amount to bet: $")
        if(bet.isdigit()): # Checks if the input is a number
            bet = int(bet)  # Converts the input to an integer

           

            if MIN_BET <= bet <= MAX_BET:
            
                break
            else:

                print(f"Bet must be between ${MIN_BET} - ${MAX_BET}.")

        else:
                
                print("Please enter a number.")



    return bet
                
     
def game(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet_amount()
        total_bet = bet * lines
        if total_bet <= balance:
            break
        else:
            print(f"Insufficient funds. Your balance is ${balance}")    

    print(f"you are playing {lines} lines with ${bet} bet. Total bet is ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)
    print(f"You won ${winnings}")
    print(f"Winning lines:", *winning_lines)

    return winnings - total_bet
     


def main():
    balance = deposit()
    while True:
        print(f"Your balance is ${balance}")
        answer = input("Press enter to play or 'q' to quit: ")

        if answer == "q":
            break
        balance += game(balance)

        if balance <= 0:
            print("You have no more money to play.")

            break



        

    print(f"Your balance is ${balance}")
    
main()