from abc import ABC, abstractmethod
from typing import Any, Dict, List
import src.utils as utils


CONFIG_PATH = "config/config.yaml"
class DataLoaderStrategy(ABC):
    
    def __init__(self, config_path: str = CONFIG_PATH):
        """
        Initialize the DataLoaderStrategy with a configuration file.

        Args:
            config_path (str): Path to the configuration file.
        """
        self.config = utils.load_config(config_path)
        self.root_path = self.config.get('paths', {}).get('root', '')
        self.data_paths = self.config.get('path_data', {})
    
    @abstractmethod
    def load_data(self, *args, **kwargs) -> List[Dict[str, Any]]:
        pass
    