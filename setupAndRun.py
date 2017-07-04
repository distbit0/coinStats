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
    if "BTC_" in market:
      coinList.append(market.replace("BTC_", "").lower())
  return coinList

def amalgamateScores():
   coinScores = {}
   coinOrderBookRatios, coinMkToVolRatios, totalMkToVolScore, totalOrderBookRatioScore = collectData()
   coinNames = getCoinNames()
   for coin in coinNames:
      orderBookRatio = avgCoinRatio = mkToVolRatio = 0
      if coin in coinOrderBookRatios:
         orderBook = coinOrderBookRatios[coin]
         orderBookRatio = orderBook/totalOrderBookRatioScore
         avgCoinRatio = orderBookRatio
      if coin in coinMkToVolRatios:
         mkToVol = coinMkToVolRatios[coin]
         mkToVolRatio = mkToVol/totalMkToVolScore
         avgCoinRatio = (orderBookRatio + mkToVolRatio) / 2
      
      coinScores[coin] = {"avg":avgCoinRatio, "mkToVol":mkToVol, "orderBook":orderBook}
   return coinScores


def displayCoinScores():
   coinScores = amalgamateScores()
   for coin in sorted(coinScores, key=lambda x: coinScores[x]["avg"]):
      avg = str(round(coinScores[coin]["avg"], 5))
      orderBook = str(round(coinScores[coin]["orderBook"], 5))
      mkToVol = str(round(coinScores[coin]["mkToVol"], 5))
      print(coin + ": \tavg: " + avg + "\torderBook: " + orderBook + "\tmkToVol: " + mkToVol)

if __name__ == "__main__":
   displayCoinScores()
