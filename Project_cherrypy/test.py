import os
import cherrypy
"""from cherrypy.process.plugins import Daemonizer
Daemonizer(cherrypy.engine).subscribe()"""

class First():
    @cherrypy.expose
    def anything(self):
        return "<H1>Test</H1>"

    @cherrypy.expose
    def index(self):
        return open("template_6/index.html")
    

if __name__ == '__main__':
    conf = {
            '/':{
                 'tools.staticdir.on':True,
                 'tools.staticdir.root':os.path.dirname(os.path.abspath(__file__)),
                 'tools.staticdir.dir':'./template_6',
            },
            '/favicon.ico':{
                            'tools.staticfile.on':True,
                            'tools.staticfile.root':os.path.dirname(os.path.abspath(__file__))+'\\template_6\\images',
                            'tools.staticfile.filename':'logo.ico'
                            }
    }
    print(os.path.abspath(__file__))
    cherrypy.config.update({'server.socket_host':'10.192.53.55',
                            'server.socket_port':3128
                            }
                            )
    print(os.path.dirname(os.path.abspath(__file__))+'\\template_6\\images')
    cherrypy.quickstart(First(),'/', conf)
    print('checked')
