import tornado.ioloop
import tornado.web
import getAvgCoinStats
import volumeToMarketCapRatio
import orderBookRatio

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()
