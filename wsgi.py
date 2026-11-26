# wsgi.py
"""
Punto de entrada para servidores WSGI de producción.

Se usa desde el contenedor:

    gunicorn --worker-class gthread --threads 100 wsgi:app

Gunicorn sirve HTTP normal (Flask); las rutas /socket.io/* las atiende
Flask-SocketIO sobre el mismo puerto, sin necesitar un worker async especial.
"""
from werkzeug.middleware.proxy_fix import ProxyFix
from app import create_app

app = create_app()
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1)
