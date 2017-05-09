###Function to set up polo API connection###
def initPoloConnection():
  from poloniex import Poloniex
  return Poloniex()
############################################s

def getCoinNames(api):
  coinList = []
  coins = api.return24hVolume()
  for market in coins:
    if "BTC_" in market and float(coins[market]["BTC"]) > 200:
      coinList.append(market)
  return coinList

#####Function to get orderbook vol up to daily extremes##############
def getOrderBookVol(api, pair):
  orderbook = api.returnOrderBook(pair, depth=10000000)
  bids, asks = [orderbook["bids"], orderbook["asks"]]
  price = (float(bids[0][0]) + float(asks[0][0])) / 2
  bidVol = askVol = 0
  
  for bid in bids:
    bidVol += float(bid[1]) * float(bid[0])

  for ask in asks:
    askVol += float(ask[1]) * price

  return bidVol/askVol
#######################################################################
    
#####Generate Coin Opportunity List#######
def getOpportunities():
  coinOpportunities = {}
  api = initPoloConnection()
  coinNames = getCoinNames(api)
  for coin in coinNames:
    coinOpportunities[coin.replace("BTC_", "").lower()] = getOrderBookVol(api, coin)
  return coinOpportunities
