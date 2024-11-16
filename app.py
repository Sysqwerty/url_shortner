from aiohttp import web

from src.conf.settings import config
from src.db import pg_context
from src.routes import setup_routes

app = web.Application()
setup_routes(app)
app['config'] = config
app.cleanup_ctx.append(pg_context)
web.run_app(app, host="localhost", port=8080)
