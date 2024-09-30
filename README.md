# Python Slot Machine Game

This project implements a simple slot machine game in Python. Users can place bets on different lines, spin the slot machine, and win or lose based on the symbols that appear on each row. The game keeps track of the player's balance and allows them to continue playing until they choose to quit.

## Features
- Bet on up to 3 lines in the slot machine.
- Symbols appear randomly, with varying frequencies.
- Winnings are calculated based on the symbol value and the bet amount.
- The game runs in the terminal/console and provides a user-friendly interface for placing bets and playing.

## Prerequisites
You need to have Python installed on your machine to run this game. The project uses Python's built-in libraries, so no additional dependencies are required.

### Installing Python
If you don't have Python installed, you can download it from [Python's official website](https://www.python.org/downloads/).

## How to Play

1. Clone the repository to your local machine:
```bash
git clone https://github.com/Poxxon/Slot-Machine.git
```
## Gameplay Instructions

1. **Deposit Money**: When you start the game, you will be prompted to enter the amount of money you want to deposit.

2. **Betting**:
    - You can bet on 1, 2, or 3 lines. The more lines you bet on, the higher your total bet will be.
    - You will also be prompted to enter your bet amount per line. The minimum bet is $1, and the maximum bet is $100.

3. **Spinning**:
    - After placing your bet, the slot machine will spin and display the symbols for each line.
    - The symbols used are:
        - **A**: High-value symbol (appears less frequently)
        - **B**, **C**, **D**: Lower-value symbols (appear more frequently)

4. **Winning**:
    - You win if the symbols in any of the lines match from left to right.
    - The winnings are calculated by multiplying the symbol's value by your bet amount.
    - The game will display your total winnings and the lines on which you won.

5. **Continue or Quit**:
    - After each spin, you can either press enter to continue playing or type `q` to quit the game.

## How It Works

### Symbol Frequency

The slot machine uses different symbols with varying frequencies, represented by a dictionary:

```python
symbol_count = {
    "A": 2,  # Rare symbol
    "B": 4,
    "C": 6,
    "D": 8   # Most common symbol
}
```
This ensures that high-value symbols appear less frequently, adding an element of randomness and difficulty.

## Winning Calculation

Each symbol has a value associated with it:

```python
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}
```
If a line contains matching symbols, your winnings are calculated by multiplying the bet amount by the symbol's value.

## Slot machine logic
- The slot machine's reels are represented by columns. Each column is randomly populated with symbols based on their defined frequency.
- The program checks each line to see if the symbols match across all columns and calculates the winnings accordingly.

## Code Breakdown
- get_slot_machine_spin(): Generates a random spin for the slot machine by selecting symbols for each column based on their defined frequencies.
- check_winnings(): Checks if any line contains matching symbols from left to right and calculates the player's winnings.
- get_bet() and get_number_of_lines(): Prompts the player to enter the number of lines to bet on and the amount to bet.
- spin(): Handles the game logic for placing a bet, spinning the reels, and calculating the player's final balance.
- main(): The main game loop where players deposit money, place bets, and either play or quit the game.

## Sample output
```bash
Enter the amount of money you want to deposit: $500
You are betting $50 on 3 lines. Total bet is equal to $150.
| A | C | D |
| B | B | B |
| D | D | C |
You won $200!
You won on lines: 2
Current balance is $550
Press enter to play (q to quit):
