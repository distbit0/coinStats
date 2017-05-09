def collectData():
   from volumeToMarketCapRatio import getCoinMkToVolRatios
   from orderBookRatio import getOpportunities
   coinOrderBookRatios = getOpportunities()
   coinMkToVolRatios = getCoinMkToVolRatios()
   avgCoinScores = {}
   totalMkToVolScore, totalOrderBookRatioScore = [sum(coinMkToVolRatios.values()), sum(coinOrderBookRatios.values())]
   return [coinOrderBookRatios, coinMkToVolRatios, totalMkToVolScore, totalOrderBookRatioScore]

def amalgamateScores(coinOrderBookRatios, coinMkToVolRatios, totalOrderBookRatioScore, totalMkToVolScore):
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


   def displayCoinScores(coinMkToVolRatios):
      for coin in sorted(coinMkToVolRatios, key=lambda x: coinMkToVolRatios[x]):
         print(coin + ": " + str(coinMkToVolRatios[coin][0]/coinMkToVolRatios[coin][1]))
      
coinOrderBookRatios, coinMkToVolRatios, totalMkToVolScore, totalOrderBookRatioScore = collectData()
avgCoinScores = amalgamateScores(coinOrderBookRatios, coinMkToVolRatios, totalOrderBookRatioScore, totalMkToVolScore)
displayCoinScores(avgCoinScores)
