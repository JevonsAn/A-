import tornado.httpserver
import tornado.web
import tornado.ioloop
import os
import json
from shortestpath import getgraph, findpath
global_values = {"topo_json": ""}


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        with open("graph.html", encoding="utf8") as f:
            content = f.read()
        self.write(content)


class JsonHandler(tornado.web.RequestHandler):

    def get(self):
        asn = self.get_argument("asn")
        self.write(asn)


class GraphDataHandler(tornado.web.RequestHandler):

    def get(self):
        optype = self.get_argument("type")
        print(optype)
        if optype == "filenames":
            files = []
            files = list(os.listdir("static/graphs/"))
            self.write(json.dumps(files))
        elif optype == "getdata":
            filename = self.get_argument("file")
            graph, height, width, s, d = getgraph("static/graphs/" + filename)
            self.write(json.dumps({"height": height, "width": width, "graph": graph, "src": list(s), "dst": list(d)}))
        elif optype == "getresult":
            filename = self.get_argument("file")
            path, time = findpath(*getgraph("static/graphs/" + filename))
            self.write(json.dumps({"path": path}))

        self.write(" ")


if __name__ == "__main__":
    # tornado.options.parse_command_line()
    settings = {
        "static_path": os.path.join(os.path.dirname(__file__), "static"),
    }
    application = tornado.web.Application(
        handlers=[
            (r"/", MainHandler),
            (r"/json", JsonHandler),
            (r"/graph", GraphDataHandler),
            # (r"/relation", RelationHandler),
            # (r"/country", CountryHandler),
            # (r"^/.*$", OtherHandler),
            # (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "/home/auto/bgpsim/web"})
        ],
        debug=True,
        **settings
    )

    http_server = tornado.httpserver.HTTPServer(application)
    # http_server.bind(65530)
    # http_server.start(0)
    http_server.listen(3333)
    tornado.ioloop.IOLoop.instance().start()
