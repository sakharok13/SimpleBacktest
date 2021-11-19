import numpy as np
import matplotlib.pyplot as plt


class Env():

    def __init__(self, data, usd_start, eth_start, current_state=0, look_back=0):
        assert(type(look_back) == int), 'Look_back should be an integer'
        assert(type(current_state) == int), 'Current_state is just an index (timestamp) of your data'

        self.init_eth = eth_start
        self.init_usd = usd_start
        self.current_state = current_state
        self.look_back = look_back
        self.data = data
        self.usd = usd_start
        self.eth = eth_start
        self.current_price = data[current_state]
        self.backtested = False

    def state_upd(self):
        self.current_state += 1
        self.current_price = self.data[self.current_state]

    def action(self, amount):
        self.amount = amount
        self.portfolio_upd(amount)
        self.state_upd()

    def portfolio_upd(self, amount):
        assert(self.usd - amount <= 0), 'Невозможен отрицательный баланс USDC'
        assert(self.eth + amount / self.current_price <= 0), 'Невозможен отрицательный баланс ETH'
        
        self.usd -= amount
        self.eth += amount / self.current_price

    def get_portfolio(self):
        return (self.usd, self.eth)

    def get_returns(self):
        return (self.usd - self.init_usd) + (self.eth - self.init_eth) * self.current_price

    def define_strategy(self, function):
        self.portfolio_history = []
        self.function = function

    def backtest(self):
        if self.look_back == 0:
            while self.current_state < len(self.data) - 1:
                self.action(
                    self.function(self.data[self.current_state],
                                  self.usd,
                                  self.eth)
                )
                self.portfolio_history.append(self.get_returns())
        elif self.look_back > 0:
            pass
        self.backtested = True

    def get_plot(self):
        assert (self.backtested == True), 'You should run backtesting first'
        plt.figure(figsize=(10, 5))
        plt.title('Portfolio value')
        plt.xlabel('Timestamps')
        plt.ylabel('USDC')
        plt.plot(self.portfolio_history)
        plt.show()
