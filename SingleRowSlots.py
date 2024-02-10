import random

MIN_DEPOSIT = 50
MIN_BET = 10
COLUMNS = 5
SLOTS_SYMBOLS = {
        'Watermelon' : 2,
        'Bell' : 3,
        'Plum' : 4,
        'Tangerine' : 5,
        'Cherries' : 6
    }

def deposit():
    while True:
        amount = input(f'How much would you like to deposit? (Min is ${MIN_DEPOSIT}). $')
        if amount.isdigit():
            amount = int(amount)

            if amount >= MIN_DEPOSIT:
                break
            else:
                print(f'Your deposit must be larger than ${MIN_DEPOSIT}')
        else:
            print('Please enter a valid number')
    return amount

def get_bet():
    while True:
        bet = input('How much money would you like to bet? (Min is $10) $')
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet:
                break
            else:
                print(f'You must bet at least ${MIN_BET}')
        else:
            print('Please enter a valid amount')
    return bet

def spin_result(slots_symbols):
    wheel = []
    for symbol, symbol_count in slots_symbols.items():
        for _ in range(symbol_count):
            wheel.append(symbol)
    
    return(random.choice(wheel))



def main():
    balance = deposit()
    bet = get_bet()
    print(spin_result(SLOTS_SYMBOLS))
    
main()

#discontinued because the random.choice for the spin result is not random.