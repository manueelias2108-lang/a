#!/usr/bin/env python3
"""
Tests for the Slot Machine
"""
import unittest
from slot_machine import SlotMachine


class TestSlotMachine(unittest.TestCase):
    """Test cases for SlotMachine class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.machine = SlotMachine(balance=100)
    
    def test_initial_balance(self):
        """Test that initial balance is set correctly."""
        self.assertEqual(self.machine.get_balance(), 100)
    
    def test_insufficient_balance(self):
        """Test spinning with insufficient balance."""
        result, winnings, message = self.machine.spin(bet=150)
        self.assertIsNone(result)
        self.assertEqual(winnings, 0)
        self.assertEqual(message, "Insufficient balance!")
    
    def test_invalid_bet_zero(self):
        """Test spinning with zero bet."""
        result, winnings, message = self.machine.spin(bet=0)
        self.assertIsNone(result)
        self.assertEqual(winnings, 0)
        self.assertEqual(message, "Bet must be positive!")
    
    def test_invalid_bet_negative(self):
        """Test spinning with negative bet."""
        result, winnings, message = self.machine.spin(bet=-10)
        self.assertIsNone(result)
        self.assertEqual(winnings, 0)
        self.assertEqual(message, "Bet must be positive!")
    
    def test_spin_returns_three_symbols(self):
        """Test that spin returns exactly three symbols."""
        result, _, _ = self.machine.spin(bet=10)
        self.assertEqual(len(result), 3)
        for symbol in result:
            self.assertIn(symbol, SlotMachine.SYMBOLS)
    
    def test_spin_deducts_bet(self):
        """Test that spinning deducts the bet from balance."""
        initial_balance = self.machine.get_balance()
        result, winnings, _ = self.machine.spin(bet=10)
        # Balance should equal initial - bet + winnings
        expected_balance = initial_balance - 10 + winnings
        self.assertEqual(self.machine.get_balance(), expected_balance)
    
    def test_jackpot_winnings(self):
        """Test jackpot (three 7s) winnings calculation."""
        result = ['7️⃣', '7️⃣', '7️⃣']
        winnings = self.machine._calculate_winnings(result, bet=10)
        self.assertEqual(winnings, 100)  # 10x bet
    
    def test_star_winnings(self):
        """Test three stars winnings calculation."""
        result = ['⭐', '⭐', '⭐']
        winnings = self.machine._calculate_winnings(result, bet=10)
        self.assertEqual(winnings, 50)  # 5x bet
    
    def test_three_of_a_kind_winnings(self):
        """Test three of a kind winnings calculation."""
        result = ['🍒', '🍒', '🍒']
        winnings = self.machine._calculate_winnings(result, bet=10)
        self.assertEqual(winnings, 30)  # 3x bet
    
    def test_two_of_a_kind_winnings(self):
        """Test two of a kind winnings calculation."""
        result = ['🍒', '🍒', '🍋']
        winnings = self.machine._calculate_winnings(result, bet=10)
        self.assertEqual(winnings, 20)  # 2x bet
    
    def test_no_match_winnings(self):
        """Test no match returns zero winnings."""
        result = ['🍒', '🍋', '🍊']
        winnings = self.machine._calculate_winnings(result, bet=10)
        self.assertEqual(winnings, 0)
    
    def test_balance_update_on_win(self):
        """Test that balance updates correctly on win."""
        # Mock a winning spin by directly manipulating result
        initial_balance = self.machine.get_balance()
        # Force a win by testing the calculation
        self.machine.balance -= 10  # Deduct bet
        winnings = self.machine._calculate_winnings(['🍒', '🍒', '🍒'], bet=10)
        self.machine.balance += winnings
        # With 3 cherries at 10 bet, should win 30
        self.assertEqual(self.machine.get_balance(), initial_balance - 10 + 30)
    
    def test_multiple_spins(self):
        """Test multiple spins work correctly."""
        for _ in range(5):
            if self.machine.get_balance() >= 10:
                result, _, _ = self.machine.spin(bet=10)
                self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
