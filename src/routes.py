from src.views import index, create_url, get_origin_url


def setup_routes(app):
    app.router.add_get('/', index, name='index')
    app.router.add_post('/', create_url)
    app.router.add_get('/{unique_code}', get_origin_url, name='get_origin_url')
