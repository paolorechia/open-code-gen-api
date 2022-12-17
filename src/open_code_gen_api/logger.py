import logging
import sys

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(sys.stdout))
