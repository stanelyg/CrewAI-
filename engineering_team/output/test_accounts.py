
import unittest
from unittest.mock import patch
from accounts import Account, get_share_price

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account()

    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 0)

    def test_deposit_positive_amount(self):
        self.account.deposit(100)
        self.assertEqual(self.account.balance, 100)

    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

    def test_withdraw_positive_amount(self):
        self.account.deposit(200)
        self.account.withdraw(100)
        self.assertEqual(self.account.balance, 100)

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(100)

    def test_withdraw_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-100)

    @patch('accounts.get_share_price', return_value=150)
    def test_buy_shares(self, mock_get_share_price):
        self.account.deposit(300)
        self.account.buy_shares('AAPL', 2)
        self.assertEqual(self.account.balance, 0)
        self.assertEqual(self.account.portfolio['AAPL'], 2)

    @patch('accounts.get_share_price', return_value=150)
    def test_buy_shares_insufficient_funds(self, mock_get_share_price):
        self.account.deposit(100)
        with self.assertRaises(ValueError):
            self.account.buy_shares('AAPL', 2)

    @patch('accounts.get_share_price', return_value=150)
    def test_sell_shares(self, mock_get_share_price):
        self.account.deposit(300)
        self.account.buy_shares('AAPL', 2)
        self.account.sell_shares('AAPL', 1)
        self.assertEqual(self.account.balance, 150)
        self.assertEqual(self.account.portfolio['AAPL'], 1)

    @patch('accounts.get_share_price', return_value=150)
    def test_sell_shares_not_enough(self, mock_get_share_price):
        with self.assertRaises(ValueError):
            self.account.sell_shares('AAPL', 1)

    @patch('accounts.get_share_price', return_value=150)
    def test_portfolio_value(self, mock_get_share_price):
        self.account.deposit(300)
        self.account.buy_shares('AAPL', 2)
        self.assertEqual(self.account.calculate_portfolio_value(), 300)

    @patch('accounts.get_share_price', side_effect=lambda symbol: {'AAPL': 150, 'TSLA': 700}.get(symbol, 0))
    def test_calculate_profit_loss(self, mock_get_share_price):
        self.account.deposit(300)
        self.account.buy_shares('AAPL', 1)
        self.assertEqual(self.account.calculate_profit_loss(), 0)
        self.account.sell_shares('AAPL', 1)
        self.assertEqual(self.account.calculate_profit_loss(), 150)

    def test_get_holdings(self):
        self.account.deposit(200)
        self.account.buy_shares('AAPL', 2)
        self.assertEqual(self.account.get_holdings(), {'AAPL': 2})

    def test_get_transactions(self):
        self.account.deposit(200)
        self.account.buy_shares('AAPL', 2)
        transactions = self.account.get_transactions()
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]['symbol'], 'AAPL')

if __name__ == '__main__':
    unittest.main()
