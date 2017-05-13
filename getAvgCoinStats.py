def collectData():
   from volToMkRatio import getCoinMkToVolRatios
   from orderBookRatio import getCoinOrderBookRatios
   coinOrderBookRatios = getCoinOrderBookRatios()
   coinMkToVolRatios = getCoinMkToVolRatios()
   totalMkToVolScore, totalOrderBookRatioScore = [sum(coinMkToVolRatios.values()), sum(coinOrderBookRatios.values())]
   return [coinOrderBookRatios, coinMkToVolRatios, totalMkToVolScore, totalOrderBookRatioScore]

def getCoinNames():
  from poloniex import Poloniex
  api =  Poloniex()
  coinList = []
  coins = api.return24hVolume()
  for market in coins:
    if "BTC_" in market and float(coins[market]["BTC"]) > 200:
      coinList.append(market.replace("BTC_", "").lower())
  return coinList

def amalgamateScores():
   coinScores = {}
   coinOrderBookRatios, coinMkToVolRatios, totalMkToVolScore, totalOrderBookRatioScore = collectData()
   coinNames = getCoinNames()
   for coin in coinNames:
      orderBookRatio = avgCoinRatio = mkToVolRatio = 0
      if coin in coinOrderBookRatios:
         orderBookRatio = coinOrderBookRatios[coin]/totalOrderBookRatioScore
         avgCoinRatio = orderBookRatio
      if coin in coinMkToVolRatios:
         mkToVolRatio = coinMkToVolRatios[coin]/totalMkToVolScore
         avgCoinRatio = (orderBookRatio + mkToVolRatio) / 2
         
      coinScores[coin] = {"avg":avgCoinRatio, "mkToVol":mkToVolRatio, "orderbook":orderBookRatio}
   return coinScores


def displayCoinScores(coinScores):
   for coin in sorted(coinScores, key=lambda x: coinScores[x]["avg"]):
      avg = str(coinScores[coin]["avg"])
      orderbook = str(coinScores[coin]["orderBook"])
      mkToVol = str(coinScores[coin]["mkToVol"])
      print(coin + ": \tAvg: " + avg + "\tOrderbook: " + orderbook + "\tmkToVol: " + mkToVol)

if __name__ == "__main__":
   avgCoinScores = amalgamateScores()
   displayCoinScores(avgCoinScores)
