#! python3
# Enter in-game sensitivity via command line to get your EDPI


def calculate_eDPI(in_game_sens, DPI):
    eDPI = int(in_game_sens * DPI)
    return eDPI

def main():
    in_game_sens_input = float(input("What is your in-game sensitivity? "))
    DPI_input = int(input("What is your DPI? "))
    user_eDPI = calculate_eDPI(in_game_sens_input, DPI_input)
    print(f'Your eDPI is: {user_eDPI}')

main()