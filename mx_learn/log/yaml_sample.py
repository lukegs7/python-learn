import logging
import yaml
from logging.config import dictConfig
from log.func import func

with open('loggerconfig.yml', 'r', encoding='utf-8') as f:
    logger_config = yaml.safe_load(f)
dictConfig(logger_config)

logger = logging.getLogger('simpleExample')

if __name__ == '__main__':
    logger.info('geshuai1992')
    func()
