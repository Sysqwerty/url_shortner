import asyncio
import sys

from aiohttp import web
import aiohttp_jinja2
import jinja2

from src.conf.settings import config, BASE_DIR
from src.db import pg_context
from src.routes import setup_routes

app = web.Application()
loader = jinja2.FileSystemLoader(str(BASE_DIR / 'src' / 'templates'))
aiohttp_jinja2.setup(app, loader=loader)
setup_routes(app)
app['config'] = config
app.cleanup_ctx.append(pg_context)

if __name__ == '__main__':
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    web.run_app(app, host="0.0.0.0", port=8080)
