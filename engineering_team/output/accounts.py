class Account:
    def __init__(self):
        self.balance = 0.0
        self.initial_deposit = 0.0
        self.portfolio = {}
        self.transactions = []

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount must be positive")
        if self.initial_deposit == 0:
            self.initial_deposit = amount
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def buy_shares(self, symbol, quantity):
        price = get_share_price(symbol)
        total_cost = price * quantity
        if total_cost > self.balance:
            raise ValueError("Insufficient funds to buy shares")
        self.balance -= total_cost
        if symbol in self.portfolio:
            self.portfolio[symbol] += quantity
        else:
            self.portfolio[symbol] = quantity
        self.transactions.append({
            'type': 'buy',
            'symbol': symbol,
            'quantity': quantity,
            'price': price
        })

    def sell_shares(self, symbol, quantity):
        if symbol not in self.portfolio or self.portfolio[symbol] < quantity:
            raise ValueError("Not enough shares to sell")
        price = get_share_price(symbol)
        self.portfolio[symbol] -= quantity
        self.balance += price * quantity
        self.transactions.append({
            'type': 'sell',
            'symbol': symbol,
            'quantity': quantity,
            'price': price
        })

    def calculate_portfolio_value(self):
        total_value = 0.0
        for symbol, quantity in self.portfolio.items():
            total_value += get_share_price(symbol) * quantity
        return total_value

    def calculate_profit_loss(self):
        current_value = self.balance + self.calculate_portfolio_value()
        return current_value - self.initial_deposit

    def get_holdings(self):
        return self.portfolio

    def get_transactions(self):
        return self.transactions


def get_share_price(symbol):
    fixed_prices = {'AAPL': 150.0, 'TSLA': 700.0, 'GOOGL': 2800.0}
    return fixed_prices.get(symbol, 0.0)

# Test the module
account = Account()
account.deposit(1000)
account.buy_shares('AAPL', 2)
account.sell_shares('AAPL', 1)
print('Balance:', account.balance)
print('Holdings:', account.get_holdings())
print('Transactions:', account.get_transactions())
print('Portfolio Value:', account.calculate_portfolio_value())
print('Profit/Loss:', account.calculate_profit_loss())