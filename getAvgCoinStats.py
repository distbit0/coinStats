def collectData():
   from orderBookRatio import getCoinOrderBookRatios
   coinOrderBookRatios = getCoinOrderBookRatios()
   return coinOrderBookRatios

def getCoinNames():
  from poloniex import Poloniex
  api =  Poloniex()
  coinList = []
  coins = api.return24hVolume()
  for market in coins:
    if "BTC_" in market:
      coinList.append(market.replace("BTC_", "").lower())
  return coinList

def amalgamateScores():
   coinScores = {}
   coinOrderBookRatios = collectData()
   coinNames = getCoinNames()
   for coin in coinNames:
      orderBookRatio = avgCoinRatio = mkToVolRatio = 0
      if coin in coinOrderBookRatios:
         orderBook = coinOrderBookRatios[coin]
         orderBookRatio = orderBook
         avgCoinRatio = orderBookRatio
      
      coinScores[coin] = {"avg":avgCoinRatio}
   return coinScores


def displayCoinScores():
   coinScores = amalgamateScores()
   for coin in sorted(coinScores, key=lambda x: coinScores[x]["avg"]):
      avg = str(round(coinScores[coin]["avg"], 5))
      print(coin + ": bid/ask Ratio: " + avg)

if __name__ == "__main__":
   displayCoinScores()
