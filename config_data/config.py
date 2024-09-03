from dataclasses import dataclass

from environs import Env
from typing import Union


@dataclass
class TgBot:
    token: str
    admin: int


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: Union[str, None]=None):
    env = Env()
    env.read_env(path)
    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN'),
            admin=env('ADMIN')
        )
    )
