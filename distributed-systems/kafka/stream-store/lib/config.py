import os
import yaml
from typing import Dict, Any
from pathlib import Path

class Config:
    """
    Configuration loader and manager for the Kafka Stream Store application.
    Loads configuration from YAML files and provides easy access to config values.
    """
    
    def __init__(self, config_file, environment: str):
        """
        Initialize the configuration loader.
        
        Args:
            config_file (str): Path to specific config file. If None, uses environment-based loading.
            environment (str): Environment name (dev, prod, test, etc.). Defaults to 'dev'.
        """
        self._config_data = {}
        self._environment = environment
        
        if config_file:
            self._load_config_file(config_file)
        else:
            self._load_environment_config()
    
    def _load_config_file(self, config_file: str):
        """Load configuration from a specific file."""
        config_path = Path(config_file)
        if not config_path.exists():
            raise FileNotFoundError(f"Configuration file not found: {config_file}")
        
        with open(config_path, 'r', encoding='utf-8') as file:
            self._config_data = yaml.safe_load(file) or {}
    
    def _load_environment_config(self):
        """Load configuration based on environment."""
        # Get the project root directory
        project_root = Path(__file__).parent.parent
        config_dir = project_root / "config"
        config_file = config_dir / f"{self._environment}.yaml"
        
        if not config_file.exists():
            raise FileNotFoundError(f"Configuration file not found: {config_file}")
        
        self._load_config_file(str(config_file))
    
    def get(self, key_path: str, default: Any = None) -> Any:
        """
        Get a configuration value using dot notation.
        
        Args:
            key_path (str): Dot-separated path to the config value (e.g., 'kafka.bootstrap_servers')
            default (Any): Default value if key is not found
            
        Returns:
            Any: The configuration value
            
        Example:
            config.get('kafka.bootstrap_servers')
            config.get('kafka.consumer.group_id', 'default-group')
        """
        keys = key_path.split('.')
        current = self._config_data
        
        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return default
        
        return current
    

    
    @property
    def environment(self) -> str:
        """Get the current environment."""
        return self._environment
    
    @property
    def raw_config(self) -> Dict[str, Any]:
        """Get the raw configuration dictionary."""
        return self._config_data.copy()


# Global configuration instance
_config_instance = None

def get_config(config_file: str = None) -> Config:
    """
    Get the global configuration instance.
    
    Args:
        config_file (str): Path to specific config file. If None, uses environment-based loading.
        environment (str): Environment name. If None, uses 'dev' or value from CONFIG_ENV env var.
        
    Returns:
        Config: The configuration instance
    """
    global _config_instance
    
    if _config_instance is None:
        # Determine environment from parameter or environment variable
        env = os.getenv('CONFIG_ENV', 'dev')
        _config_instance = Config(config_file=config_file, environment=env)
    
    return _config_instance

def reload_config(config_file: str = None, environment: str = None):
    """
    Reload the configuration (useful for tests or config changes).
    
    Args:
        config_file (str): Path to specific config file
        environment (str): Environment name
    """
    global _config_instance
    _config_instance = None
    return get_config(config_file=config_file, environment=environment)