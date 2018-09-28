# Enable Flask's debugging features.
import os
# DEBUG = True
class Config(object):
    """Parent configuration class."""
    DEBUG = False


class TestingConfig(Config):
    """Testing Configurations."""
    TESTING = True

app_config = {
    'testing': TestingConfig
    
}