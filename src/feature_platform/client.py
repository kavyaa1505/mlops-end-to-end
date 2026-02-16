from pipelines.training_pipeline import run_training_pipeline
from utils.config_loader import load_config


class FeatureClient:
    """
    Public API for the Feature Platform.
    """

    def __init__(self, config_path: str = "config.yml"):
        self.config = load_config(config_path)

    def get_features(self):
        """
        Return governed, validated feature DataFrame.
        """
        return run_training_pipeline(self.config)
