#!/usr/bin/python3

import pip

def install(package):
   pip3.main(['install', package])

def installModules():
   try:
      import poloniex
   except:
      install("poloniex")

def runCoinStats():
   import getAvgCoinStats
   getAvgCoinStats.displayCoinScores()

if __name__ == '__main__':
   installModules()
   runCoinStats()
   
