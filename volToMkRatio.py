minVol = 200
period = 10 * 86400

def representsFloat(s):
    try: 
        float(s)
        return True
    except ValueError: return False
        
def getCoinNames(minVol):
  from poloniex import Poloniex
  api =  Poloniex()
  coinList = []
  coins = api.return24hVolume()
  for market in coins:
    if "BTC_" in market and float(coins[market]["BTC"]) > minVol:
      coinList.append(market.replace("BTC_", "").lower())
  return coinList
  
def getAllCoinData():
   import requests
   return requests.get("http://coinmarketcap.northpole.ro/api/v5/all.json").json() 
   
def getGlobalData():
  import requests
  globalData = requests.get("https://api.coinmarketcap.com/v1/global/").json()
  return [globalData["total_market_cap_usd"], globalData["total_24h_volume_usd"]]
    
def getBitcoinPrice():
   import requests
   return requests.get("https://blockchain.info/ticker").json()["USD"]["last"]
   
def getCoinData(coin, allCoinData, bitcoinPrice, period):
   import poloniex
   import time
   currentTime = time.time()
   startTime = currentTime - period
   polo = poloniex.Poloniex()
   coinMk = False
   coinVolume = 0
   try:
      coinData = [currency for currency in allCoinData["markets"] if currency["symbol"].lower() == coin][0]
   except: return [0,0]
   
   for day in polo.returnChartData(pair="BTC_" + coin.upper(), start=startTime, end=currentTime, period=86400):
      coinVolume += float(day["volume"]) * bitcoinPrice
   coinVolume /= (period/86400)
      
   if representsFloat(coinData["marketCap"]["usd"]) and float(coinData["marketCap"]["usd"]) > 0:
      coinMk = float(coinData["marketCap"]["usd"])
      
   if coinMk and coinVolume:
      return [coinMk, coinVolume]
   else:
      return [0, 0]

def getCoinMkToVolRatio(coinData, globalData):
  globalMk, globalVol = globalData
  coinMk, coinVol = coinData
  coinVolumeRatio = coinVol / globalVol
  coinMarketCapRatio = coinMk/ globalMk
  return coinVolumeRatio / coinMarketCapRatio

def getCoinMkToVolRatios():
   bitcoinPrice = getBitcoinPrice()
   coinNames = getCoinNames(minVol)
   allCoinData = getAllCoinData()
   globalData = getGlobalData()
   coinMkToVolRatios = {}
   for coin in coinNames:
      coinData = getCoinData(coin, allCoinData, bitcoinPrice, period)
      if coinData[0] != 0:
         coinMkToVolRatios[coin] = getCoinMkToVolRatio(coinData, globalData)
   return coinMkToVolRatios
