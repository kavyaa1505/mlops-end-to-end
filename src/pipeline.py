from utils.config_loader import load_config
from pipelines.training_pipeline import run_training_pipeline

def run_pipeline():
    config = load_config()
    print("🚀 Starting pipeline:", config["project"]["name"])

    run_training_pipeline(config)

    print("🎉 Pipeline completed successfully")

if __name__ == "__main__":
    run_pipeline()
