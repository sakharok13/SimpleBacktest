def strategy(price, usd, eth):
  if usd - eth*price > 0:
    return ((usd - eth * price) / 2)
  elif usd - eth*price < 0:
    return  ((usd - eth*price) / 2)
  else:
    return(0)
