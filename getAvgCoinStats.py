def collectData():
   from volumeToMarketCapRatio import getCoinMkToVolRatios
   from orderBookRatio import getOpportunities
   coinOrderBookRatios = getOpportunities()
   coinMkToVolRatios = getCoinMkToVolRatios()
   totalMkToVolScore, totalOrderBookRatioScore = [sum(coinMkToVolRatios.values()), sum(coinOrderBookRatios.values())]
   return [coinOrderBookRatios, coinMkToVolRatios, totalMkToVolScore, totalOrderBookRatioScore]

def getArguments():
   import sys
   arguments = sys.argv
   arguments.append("")
   return arguments[1]
      
def amalgamateScores():
   avgCoinScores = {}
   coinOrderBookRatios, coinMkToVolRatios, totalMkToVolScore, totalOrderBookRatioScore = collectData()
   argument = getArguments()
   if argument == "" or argument == "orderbook":
      for coin in coinOrderBookRatios:
         if coinOrderBookRatios[coin] > 1:
            if coin in avgCoinScores:
               avgCoinScores[coin][0], avgCoinScores[coin][1] = [coinOrderBookRatios[coin]/totalOrderBookRatioScore, avgCoinScores[coin][1] + 1]
            else:
               avgCoinScores[coin] = [coinOrderBookRatios[coin]/totalOrderBookRatioScore, 1]
            
   if argument == "" or argument == "mktovol":
      for coin in coinMkToVolRatios:
         if coinMkToVolRatios[coin] > 1:
            if coin in avgCoinScores:
               avgCoinScores[coin][0], avgCoinScores[coin][1] = [coinMkToVolRatios[coin]/totalMkToVolScore, avgCoinScores[coin][1] + 1]
            else:
               avgCoinScores[coin] = [coinMkToVolRatios[coin]/totalMkToVolScore, 1]
            
   return avgCoinScores


def displayCoinScores(coinMkToVolRatios):
   for coin in sorted(coinMkToVolRatios, key=lambda x: coinMkToVolRatios[x][0]/coinMkToVolRatios[x][1]):
      print(coin + ": " + str(coinMkToVolRatios[coin][0]/coinMkToVolRatios[coin][1]))

avgCoinScores = amalgamateScores()
displayCoinScores(avgCoinScores)
