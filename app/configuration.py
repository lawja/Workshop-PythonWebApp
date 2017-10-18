# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

class Config(object):
    """
    Configuration base, for all environments.
    """
    DEBUG = False

class ProductionConfig(Config):
    DATABASE_URI = ''

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_PATH = 'example.db'
    BLOG_KEY = "psswd"

class TestingConfig(Config):
    TESTING = True
