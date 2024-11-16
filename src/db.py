from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


async def pg_context(app):
    conf = app['config']['postgres']
    url_db = f"postgresql://{conf['user']}:{conf['password']}@{conf['host']}/{conf['database']}"
    DBSession = sessionmaker(bind=create_engine(url_db))
    session = DBSession()
    app['db_session'] = session
    yield
    app['db_session'].close()
