# 🎰 Slot Machine

A simple command-line slot machine game implemented in Python.

## Features

- 3-reel slot machine with 6 different symbols
- Multiple payout tiers based on matching symbols
- Balance tracking and betting system
- Interactive command-line interface

## Symbols

- 🍒 Cherry
- 🍋 Lemon
- 🍊 Orange
- 🍇 Grapes
- ⭐ Star
- 7️⃣ Lucky Seven

## Payouts

- **3x 7️⃣** = 10x bet (JACKPOT!)
- **3x ⭐** = 5x bet
- **3x any symbol** = 3x bet
- **2x any symbol** = 2x bet

## Usage

Run the slot machine game:

```bash
python3 slot_machine.py
```

The game starts with a balance of $100. Enter your bet amount for each spin, or type 'q' to quit.

## Testing

Run the test suite:

```bash
python3 test_slot_machine.py
```

Or with verbose output:

```bash
python3 test_slot_machine.py -v
```

## Requirements

- Python 3.6 or higher