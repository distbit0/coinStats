import tornado.ioloop
import tornado.web
from getAvgCoinStats import amalgamateScores as getAvgCoinStats
import json

class getCoinStats(tornado.web.RequestHandler):
    def get(self):
        requestedData = self.get_argument("stat", "avg")
        if requestedData == "avg":
            self.write(getAvgCoinStats())
        elif requestedData == "orderbook":
            self.write(getAvgCoinStats("orderbook"))
        elif requestedData == "mktovol":
            self.write(getAvgCoinStats("mktovol"))
            
class getHomePage(tornado.web.RequestHandler):
    def get(self):
        requestedData = self.get_argument("stat", "avg")
        if requestedData == "avg":
            self.write(getAvgCoinStats())
        elif requestedData == "orderbook":
            self.write(getAvgCoinStats("orderbook"))
        elif requestedData == "mktovol":
            self.write(getAvgCoinStats("mktovol"))

def make_app():
    return tornado.web.Application([
        (r"/stats/", getCoinStats),
        (r"/", getHomePage),
        (r"/index.html", web.StaticFileHandler, {"path": "index.html"}),
        (r"/js.js", web.StaticFileHandler, {"path": "js.js"}),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()
