import tornado.ioloop
import tornado.web
from tornado import web
from getAvgCoinStats import amalgamateScores as getAvgCoinStats

class getCoinStats(tornado.web.RequestHandler):
    def get(self):
        self.write(getAvgCoinStats())

def make_app():
    return tornado.web.Application([
        (r"/stats/", getCoinStats),
        (r"/index.html", web.StaticFileHandler, {"path": "index.html"}),
        (r"/js.js", web.StaticFileHandler, {"path": "js.js"}),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()
