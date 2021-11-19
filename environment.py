import numpy as np


class env(object):
    def __init__(self, look_back, data, usd_start, eth_start, current_state):
        self.current_state = current_state
        self.look_back = look_back
        self.data = data
        self.usd_start = usd_start
        self.eth_start = eth_start
        self.current_price = data[current_state]

    def state_upd(self):
        self.current_state += 1
        self.current_price = self.data[self.current_state]

    def action(self, amount):
        self.amount = amount

    def portfolio_upd(self, amount):
        self.usd_start -= amount
        self.eth_start += amount


