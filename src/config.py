import json
from pathlib import Path

from platformdirs import user_data_dir


class Config:
    config_dir = Path(user_data_dir('bot', 'enotify'))
    file_name = 'config.json'
    config_file = config_dir.joinpath(file_name)

    @classmethod
    def read(cls):
        if not cls.config_file.exists():
            raise FileNotFoundError('No config file!')

        return json.loads(cls.config_file.read_text())

    @classmethod
    def store(cls, token=None, user_id=None):
        if not cls.config_file.exists():
            cls.init_config()

        data = json.loads(cls.config_file.read_text())

        if token is not None:
            data['token'] = token

        if user_id is not None:
            data['user_id'] = user_id

        with cls.config_file.open('w') as cfg:
            cfg.write(json.dumps(data, indent=4))

    @classmethod
    def init_config(cls):
        cls.config_dir.mkdir(parents=True)

        data = {
            'token': None,
            'user_id': None
        }

        with cls.config_file.open('w') as cfg:
            cfg.write(json.dumps(data, indent=4))

    @classmethod
    def get_path(cls):
        return str(cls.config_file)
