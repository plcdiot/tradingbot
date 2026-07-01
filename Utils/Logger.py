import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

def get_logger(name):
 p=Path('logs');p.mkdir(exist_ok=True);l=logging.getLogger(name)
 if l.handlers:return l
 l.setLevel(logging.INFO);f=logging.Formatter('%(asctime)s %(levelname)s %(message)s');
 h=RotatingFileHandler(p/'tradingbot.log',maxBytes=2000000,backupCount=5);h.setFormatter(f);l.addHandler(h);return l
