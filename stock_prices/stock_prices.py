#!/usr/bin/python

import argparse

def find_max_profit(prices, cmin=None, cmax=None):
  for i in range(len(prices)):
    price = prices[i]
    if cmin and (not cmax or (price - cmin) > cmax):
      cmax = price - cmin
    if not cmin or (i < len(prices) - 1 and price < cmin):
      cmin = price
  return cmax

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
