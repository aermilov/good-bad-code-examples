import logging

from adapter.db import insert
from adapter.logger import LoggerAdapter, ThirdPartyLogger

logger = logging.getLogger('MyApp')
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

insert(LoggerAdapter(ThirdPartyLogger()))
