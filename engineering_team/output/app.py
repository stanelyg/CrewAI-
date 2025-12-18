import gradio as gr
from accounts import Account

account = Account()

def create_account(initial_deposit):
    try:
        account.deposit(initial_deposit)
        return f"Account created with initial deposit: ${initial_deposit}"
    except ValueError as e:
        return str(e)

def deposit_funds(amount):
    try:
        account.deposit(amount)
        return f"Deposited: ${amount}"
    except ValueError as e:
        return str(e)

def withdraw_funds(amount):
    try:
        account.withdraw(amount)
        return f"Withdrew: ${amount}"
    except ValueError as e:
        return str(e)

def buy_shares(symbol, quantity):
    try:
        account.buy_shares(symbol, quantity)
        return f"Bought {quantity} shares of {symbol}"
    except ValueError as e:
        return str(e)

def sell_shares(symbol, quantity):
    try:
        account.sell_shares(symbol, quantity)
        return f"Sold {quantity} shares of {symbol}"
    except ValueError as e:
        return str(e)

def get_holdings():
    return account.get_holdings()

def get_transactions():
    return account.get_transactions()

def portfolio_value():
    return account.calculate_portfolio_value()

def profit_loss():
    return account.calculate_profit_loss()

iface = gr.Interface(
    fn=create_account,
    inputs=gr.Number(label="Initial Deposit"),
    outputs="text",
    description="Create a new trading account with an initial deposit."
)

deposit_interface = gr.Interface(
    fn=deposit_funds,
    inputs=gr.Number(label="Deposit Amount"),
    outputs="text",
    description="Deposit funds into your account."
)

withdraw_interface = gr.Interface(
    fn=withdraw_funds,
    inputs=gr.Number(label="Withdraw Amount"),
    outputs="text",
    description="Withdraw funds from your account."
)

buy_interface = gr.Interface(
    fn=buy_shares,
    inputs=[gr.Textbox(label="Share Symbol"), 
            gr.Number(label="Quantity")],
    outputs="text",
    description="Buy shares."
)

sell_interface = gr.Interface(
    fn=sell_shares,
    inputs=[gr.Textbox(label="Share Symbol"), 
            gr.Number(label="Quantity")],
    outputs="text",
    description="Sell shares."
)

holdings_interface = gr.Interface(
    fn=get_holdings,
    inputs=None,
    outputs="text",
    description="Get current holdings in your account."
)

transactions_interface = gr.Interface(
    fn=get_transactions,
    inputs=None,
    outputs="text",
    description="Get transaction history."
)

portfolio_value_interface = gr.Interface(
    fn=portfolio_value,
    inputs=None,
    outputs="text",
    description="Get current portfolio value."
)

profit_loss_interface = gr.Interface(
    fn=profit_loss,
    inputs=None,
    outputs="text",
    description="Get profit or loss from the initial deposit."
)

gr.TabbedInterface(
    [iface, deposit_interface, withdraw_interface, 
     buy_interface, sell_interface, holdings_interface, 
     transactions_interface, portfolio_value_interface, 
     profit_loss_interface],
    ["Create Account", "Deposit Funds", "Withdraw Funds", 
     "Buy Shares", "Sell Shares", "Holdings", 
     "Transactions", "Portfolio Value", "Profit/Loss"]
).launch()