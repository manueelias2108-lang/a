#!/usr/bin/env python3
"""
Simple Slot Machine Implementation
"""
import random


class SlotMachine:
    """A simple slot machine with three reels."""
    
    SYMBOLS = ['🍒', '🍋', '🍊', '🍇', '⭐', '7️⃣']
    
    def __init__(self, balance=100):
        """Initialize slot machine with a starting balance."""
        self.balance = balance
        self.reels = 3
    
    def spin(self, bet=10):
        """
        Spin the slot machine.
        
        Args:
            bet: Amount to bet on this spin
            
        Returns:
            tuple: (result list, winnings, message)
        """
        if bet > self.balance:
            return None, 0, "Insufficient balance!"
        
        if bet <= 0:
            return None, 0, "Bet must be positive!"
        
        # Deduct bet
        self.balance -= bet
        
        # Spin reels
        result = [random.choice(self.SYMBOLS) for _ in range(self.reels)]
        
        # Check for wins
        winnings = self._calculate_winnings(result, bet)
        self.balance += winnings
        
        # Create message
        if winnings > 0:
            message = f"WIN! You won ${winnings}!"
        else:
            message = "No win this time."
        
        return result, winnings, message
    
    def _calculate_winnings(self, result, bet):
        """Calculate winnings based on the result."""
        # Three of a kind
        if result[0] == result[1] == result[2]:
            if result[0] == '7️⃣':
                return bet * 10  # Jackpot!
            elif result[0] == '⭐':
                return bet * 5
            else:
                return bet * 3
        
        # Two of a kind
        if result[0] == result[1] or result[1] == result[2] or result[0] == result[2]:
            return bet * 2
        
        return 0
    
    def get_balance(self):
        """Return current balance."""
        return self.balance


def main():
    """Run the slot machine game."""
    print("=" * 40)
    print("      🎰 SLOT MACHINE 🎰")
    print("=" * 40)
    print("\nSymbols: " + " ".join(SlotMachine.SYMBOLS))
    print("\nPayouts:")
    print("  3x 7️⃣  = 10x bet (JACKPOT!)")
    print("  3x ⭐ = 5x bet")
    print("  3x any = 3x bet")
    print("  2x any = 2x bet")
    print("=" * 40)
    
    machine = SlotMachine(balance=100)
    
    while True:
        print(f"\nCurrent balance: ${machine.get_balance()}")
        
        if machine.get_balance() <= 0:
            print("\n💸 You're out of money! Game over.")
            break
        
        user_input = input("\nEnter bet amount (or 'q' to quit): ").strip()
        
        if user_input.lower() == 'q':
            print(f"\nThanks for playing! Final balance: ${machine.get_balance()}")
            break
        
        try:
            bet = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        result, winnings, message = machine.spin(bet)
        
        if result is None:
            print(f"❌ {message}")
            continue
        
        print(f"\n{'  '.join(result)}")
        print(message)


if __name__ == "__main__":
    main()
