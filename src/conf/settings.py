import pathlib
import yaml

BASE_DIR = pathlib.Path(__file__).parent.parent.parent
config_path = BASE_DIR / 'conf' / 'config.yaml'


def get_config(path):
    with open(path) as f:
        config = yaml.safe_load(f)
    return config


config = get_config(config_path)
user = config['postgres']['user']
password = config['postgres']['password']
host = config['postgres']['host']
database = config['postgres']['database']
config['db_url'] = f'postgresql://{user}:{password}@{host}/{database}'
print(config['postgres']['database'])
