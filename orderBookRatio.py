orderBookDepth = 0.2
###Function to set up polo API connection###
def initPoloConnection():
  from poloniex import Poloniex
  return Poloniex()
############################################

def getCoinNames():
  api = initPoloConnection()
  coinList = []
  coins = api.return24hVolume()
  for market in coins:
    if "BTC_" in market and float(coins[market]["BTC"]) > 100:
      coinList.append(market)
  return coinList

#####Function to get orderbook vol up to daily extremes##############
def getOrderBookVol(pair):
  api = initPoloConnection()
  orderBook = api.returnOrderBook(pair, depth=10000000)
  bids, asks = [orderBook["bids"], orderBook["asks"]]
  price = (float(bids[0][0]) + float(asks[0][0])) / 2
  bidLimit, askLimit = [price - price * orderBookDepth, price + price * orderBookDepth]
  bidVol = askVol = 0
  
  for bid in bids:
    if float(bid[0]) >= bidLimit:
      bidVol += float(bid[1]) * float(bid[0])

  for ask in asks:
    if float(ask[0]) <= askLimit:
      askVol += float(ask[1]) * price

  return bidVol/askVol
#######################################################################
    
#####Generate Coin Opportunity List#######
def getCoinOrderBookRatios():
  coinOpportunities = {}
  api = initPoloConnection()
  coinNames = getCoinNames()
  for coin in coinNames:
    coinOpportunities[coin.replace("BTC_", "").lower()] = getOrderBookVol(coin)
  return coinOpportunities
