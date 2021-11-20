# SimpleBacktest
Single-currency simple backtest with custom strategy.

Your strategy should be a function F : R^3 -> R

Example: your strategy just keeps the USDC part
of portfolio equal to ETH part

F(current_price = 100, usdc = 10000, eth = 2) -> 4900
which means
you have to buy 4900 / 100 = 49
of ETH to have 5100 usdc and 51 eth

Put your strategy_name.py file in the strategies directory

Get your plot of backtesting by 

python main.py --strategy strategy_name --usdc_start your_usdc --eth_start your_eth

Env() has the following methods: 

state_upd() - move to the next timestamp\
action(amount) - buy or sell amount of currency (depends on the sign)\
portfolio_upd() - update your portfolio\
get_payoff() - get the last state of portfolio\
define_strategy(func) - used to just define your strategy\
backtest() - run the whole thing \
get_plot - plot of your portfolio through time