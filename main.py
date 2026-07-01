"""
Application entry point.
"""
from src.Utils.logger import get_logger
from config.settings import Settings

logger = get_logger(__name__)

def main():
    settings = Settings()
    logger.info("Trading Bot Pro starting...")
    logger.info("Environment loaded.")
    print("Trading Bot Pro v1.0.0")

if __name__ == "__main__":
    main()
