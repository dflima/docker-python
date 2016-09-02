from app import app
import cherrypy

if __name__ == '__main__':

    cherrypy.tree.graft(app, "/")

    cherrypy.server.unsubscribe()

    server = cherrypy._cpserver.Server()

    server.socket_host = "0.0.0.0"
    server.socket_port = 80
    server.thread_pool = 30

    # For SSL Support
    # server.ssl_module            = 'pyopenssl'
    # server.ssl_certificate       = 'ssl/certificate.crt'
    # server.ssl_private_key       = 'ssl/private.key'
    # server.ssl_certificate_chain = 'ssl/bundle.crt'

    server.subscribe()

    cherrypy.engine.start()
    cherrypy.engine.block()
