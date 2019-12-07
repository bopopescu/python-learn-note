#!/usr/python/bin/python

import logging
import logging.config

# logging.basicConfig(filename='app.log', level=logging.INFO)
logging.config.fileConfig("logger_config_file")

logging.debug('debug message')
logging.info('info message')
logging.warning('warn message')
logging.error('error message')
logging.critical('critical message')
