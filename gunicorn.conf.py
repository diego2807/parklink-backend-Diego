bind = '127.0.0.1:8000'        # solo local; Nginx es la puerta de entrada
workers = 2                    # 2 workers para cuidar la RAM de la instancia
worker_class = 'gthread'       # necesario para que Flask-SocketIO atienda /socket.io/*
threads = 100                  # hilos concurrentes por worker (según tu wsgi.py)
timeout = 30
accesslog = '-'                # envía los logs a journald (systemd)
errorlog = '-'
loglevel = 'info'
