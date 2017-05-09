def collectData():
   from volumeToMarketCapRatio import getCoinMkToVolRatios
   from orderBookRatio import getOpportunities
   coinOrderBookRatios = getOpportunities()
   coinMkToVolRatios = getCoinMkToVolRatios()
   totalMkToVolScore, totalOrderBookRatioScore = [sum(coinMkToVolRatios.values()), sum(coinOrderBookRatios.values())]
   return [coinOrderBookRatios, coinMkToVolRatios, totalMkToVolScore, totalOrderBookRatioScore]

def amalgamateScores():
   avgCoinScores = {}
   coinOrderBookRatios, coinMkToVolRatios, totalMkToVolScore, totalOrderBookRatioScore = collectData()
   for coin in coinOrderBookRatios:
      if coin in avgCoinScores:
         avgCoinScores[coin][0], avgCoinScores[coin] = [coinOrderBookRatios[coin]/totalOrderBookRatioScore, 1]
      else:
         avgCoinScores[coin] = [coinOrderBookRatios[coin]/totalOrderBookRatioScore, 1]
         
   for coin in coinMkToVolRatios:
      if coin in avgCoinScores:
         avgCoinScores[coin][0], avgCoinScores[coin] = [coinMkToVolRatios[coin]/totalMkToVolScore, 1]
      else:
         avgCoinScores[coin] = [coinMkToVolRatios[coin]/totalMkToVolScore, 1]
   return avgCoinScores


def displayCoinScores(coinMkToVolRatios):
   for coin in sorted(coinMkToVolRatios, key=lambda x: coinMkToVolRatios[x]):
      print(coin + ": " + str(coinMkToVolRatios[coin][0]/coinMkToVolRatios[coin][1]))

avgCoinScores = amalgamateScores()
displayCoinScores(avgCoinScores)
