def collectData():
   from volumeToMarketCapRatio import getCoinMkToVolRatios
   from orderBookRatio import getOpportunities
   coinOrderBookRatios = removeBearishCoins(getOpportunities())
   coinMkToVolRatios = removeBearishCoins(getCoinMkToVolRatios())
   totalMkToVolScore, totalOrderBookRatioScore = [sum(coinMkToVolRatios.values()), sum(coinOrderBookRatios.values())]
   return [coinOrderBookRatios, coinMkToVolRatios, totalMkToVolScore, totalOrderBookRatioScore]

def getArguments():
   import sys
   arguments = sys.argv
   arguments.extend(["", "", ""])
   return arguments

def removeBearishCoins(coinScores):
   strippedCoinScores = {}
   arguments = getArguments()
   for coin in coinScores:
      if coinScores[coin] > 1 or not "bullish" in arguments:
         strippedCoinScores[coin] = coinScores[coin]
   return strippedCoinScores
         

def amalgamateScores():
   avgCoinScores = {}
   coinOrderBookRatios, coinMkToVolRatios, totalMkToVolScore, totalOrderBookRatioScore = collectData()
   arguments = getArguments()
   if not "mktovol" in arguments:
      for coin in coinOrderBookRatios:
         if coin in avgCoinScores:
            avgCoinScores[coin][0], avgCoinScores[coin][1] = [coinOrderBookRatios[coin]/totalOrderBookRatioScore, avgCoinScores[coin][1] + 1]
         else:
            avgCoinScores[coin] = [coinOrderBookRatios[coin]/totalOrderBookRatioScore, 1]
            
   if not "orderbook" in arguments:
      for coin in coinMkToVolRatios:
         if coin in avgCoinScores:
            avgCoinScores[coin][0], avgCoinScores[coin][1] = [coinMkToVolRatios[coin]/totalMkToVolScore, avgCoinScores[coin][1] + 1]
         else:
            avgCoinScores[coin] = [coinMkToVolRatios[coin]/totalMkToVolScore, 1]
            
   return avgCoinScores


def displayCoinScores(coinMkToVolRatios):
   for coin in sorted(coinMkToVolRatios, key=lambda x: coinMkToVolRatios[x][0]/coinMkToVolRatios[x][1]):
      print(coin + ": " + str(coinMkToVolRatios[coin][0]/coinMkToVolRatios[coin][1]))

if __name__ == "__main__":
   avgCoinScores = amalgamateScores()
   displayCoinScores(avgCoinScores)
