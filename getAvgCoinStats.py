from volumeToMarketCapRatio import getCoinMkToVolRatios
from orderBookRatio import getOpportunities
coinOrderBookRatios = getOpportunities()
coinMkToVolRatios = getCoinMkToVolRatios()
avgCoinScores = {}
totalMkToVolScore = sum(coinMkToVolRatios.values())
totalOrderBookRatioScore = sum(coinOrderBookRatios.values())
for coin in coinOrderBookRatios:
   if coin in avgCoinScores:
      avgCoinScores[coin][0] += coinOrderBookRatios[coin]/totalOrderBookRatioScore
      avgCoinScores[coin][1] += 1
   else:
      avgCoinScores[coin] = [coinOrderBookRatios[coin]/totalOrderBookRatioScore, 1]
      
for coin in coinMkToVolRatios:
   if coin in avgCoinScores:
      avgCoinScores[coin][0] += coinMkToVolRatios[coin]/totalMkToVolScore
      avgCoinScores[coin][1] += 1
   else:
      avgCoinScores[coin] = [coinMkToVolRatios[coin]/totalMkToVolScore, 1]


def displayCoinScores(coinMkToVolRatios):
   for coin in sorted(coinMkToVolRatios, key=lambda x: coinMkToVolRatios[x]):
      print(coin + ": " + str(coinMkToVolRatios[coin][0]/coinMkToVolRatios[coin][1]))
      
displayCoinScores(avgCoinScores)
