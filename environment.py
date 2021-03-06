import matplotlib.pyplot as plt
from mock import mock
class Env():
    # usd_start, eth_start are your initial tokens
    # data[current_state] - starting price on the exchange
    # change data = mock() to test your strategy on your own data
    def __init__(self, usd_start, eth_start, current_state=0, look_back=0, data = mock()):
        assert(type(look_back) == int), 'look_back should be an integer'
        assert(type(current_state) == int), 'current_state is just an index (timestamp) of your data'

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
        assert(self.usd - amount >= 0), 'Negative USDC is not supported'
        assert(self.eth + amount / self.current_price >= 0), 'Negative ETH is not supported'

        self.usd -= amount
        self.eth += amount / self.current_price

    def get_portfolio(self):
        return (self.usd, self.eth)

    def get_payoff(self):
        return (self.usd) + (self.eth) * self.current_price

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
                self.portfolio_history.append(self.get_payoff())
        elif self.look_back > 0:
            assert(0 == 1), 'look_back > 0 is not supported'
        self.backtested = True

    def get_plot(self):
        assert (self.backtested == True), 'You should run backtesting first'
        plt.figure(figsize=(10, 8))
        plt.title('Portfolio value')
        plt.xlabel('Timestamps')
        plt.ylabel('USDC')
        plt.plot(self.portfolio_history, 'k')
        plt.show()
