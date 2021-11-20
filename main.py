import argparse
from environment import Env
import strategies
def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--strategy',
        help='Name of a strategy in the strategies directory',
        required=True
    )
    parser.add_argument(
        '--usdc_start',
        help='Initial USDC',
        required=True
    )
    parser.add_argument(
        '--eth_start',
        help='Initial ETH',
        required=True
    )
    # parser.add_argument(
    #     '--data',
    #     help='Path to data',
    #     required=True
    # )
    # parser.add_argument(
    #     '--look_back',
    #     help='How far you want to look at the past',
    #     required=True
    # )
    return parser.parse_args()

def main():
    args = _parse_args()
    environ = Env(float(args.usdc_start), float(args.eth_start))
    environ.define_strategy(getattr(strategies, args.strategy))
    environ.backtest()
    environ.get_plot()

if __name__ == '__main__':
    main()



