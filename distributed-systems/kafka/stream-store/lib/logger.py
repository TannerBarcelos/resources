import logging
from typing import Optional

class Logger:
    """Singleton logger class to ensure consistent logging configuration across the application."""
    
    _instance: Optional['Logger'] = None
    _logger: Optional[logging.Logger] = None
    
    def __new__(cls) -> 'Logger':
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self) -> None:
        if self._logger is None:
            self._setup_logger()
    
    def _setup_logger(self) -> None:
        """Configure the logger with consistent formatting and level."""
        logging.basicConfig(
            level=logging.INFO, 
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self._logger = logging.getLogger('kafka-stream-store')
    
    def get_logger(self) -> logging.Logger:
        """Get the configured logger instance."""
        if self._logger is None:
            self._setup_logger()
        return self._logger


# Convenience function to get the logger instance
def get_logger() -> logging.Logger:
    """Get the singleton logger instance."""
    return Logger().get_logger()