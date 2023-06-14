"""cfg.py"""
import configparser
import os


class Config:

    def __init__(self):
        self._config = configparser.ConfigParser()
        self._config.read(os.path.dirname(os.path.realpath(__file__)) + '/config.ini')
        self._atlas_config = self._config['atlas']

    @property
    def atlas_config(self):
        return self._atlas_config


config = Config()