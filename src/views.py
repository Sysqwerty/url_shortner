import string
import random

import aiohttp
import aiohttp_jinja2
from aiohttp import web

from src.models import Proxy

@aiohttp_jinja2.template('index.html')
async def index(request):
    domain = request.app['config']['domain']['schema'] + '://' + request.app['config']['domain']['host'] + '/'

    code = request.query.get('code')
    error = request.query.get('error')
    return {"title": "URL Shortner", "code": code, "error": error, "domain": domain}

async def generate_code(session, n=3):
    code = ""

    for i in range(n-1):
        code += random.choice(string.ascii_letters)

    code += str(random.randint(0, 9))

    is_exist = bool(session.query(Proxy).filter(Proxy.unique_code == code).first())

    if is_exist:
        return generate_code(session, n)

    return code


async def create_url(request):
    print("run create_url")
    data = await request.post()
    origin_url = data["origin_url"]
    session = request.app['db_session']
    item = session.query(Proxy).filter(Proxy.origin_url == origin_url).first()
    if item is None:
        code = await generate_code(session)
        new_item = Proxy(origin_url=origin_url, unique_code=code)
        request.app['db_session'].add(new_item)
        request.app['db_session'].commit()
    else:
        code = item.unique_code

    url = request.app.router['index'].url_for().with_query({'code': code})
    return aiohttp.web.HTTPFound(location=url)


async def get_origin_url(request):
    unique_code = request.match_info.get('unique_code')
    session = request.app['db_session']
    item = session.query(Proxy).filter(Proxy.unique_code == unique_code).first()

    if not item:
        url = request.app.router['index'].url_for().with_query({'error': 404})
        return aiohttp.web.HTTPFound(location=url)

    return aiohttp.web.HTTPFound(location=item.origin_url)


